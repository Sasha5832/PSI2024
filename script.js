/* ---------- KONFIG ---------- */
const API_URL   = 'http://localhost:8000/predict'; // ← zmień, jeśli inny host
const MAX_FILES = 10;

/* ---------- DOM ---------- */
const input     = document.getElementById('image-upload');
const grid      = document.getElementById('preview-container');
const runBtn    = document.getElementById('run-btn');
const btnBar    = document.getElementById('image-buttons');
const detailBox = document.getElementById('detail-box');

/* ---------- DANE ---------- */
let files  = [];          // File[]
const store = [];         // [{detections, unique, fileName}]

/* ---------- OBSŁUGA ZMIANY ROZMIARU MINIATUR ---------- */
const ro = new ResizeObserver(entries => {
  for (const e of entries) {
    const idx = +e.target.dataset.idx;           // nr obrazka
    if (store[idx]?.detections) {
      drawBoxes(idx, store[idx].detections);     // narysuj ponownie
    }
  }
});

/* ---------- PODGLĄD MINIATUR ---------- */
input.addEventListener('change', () => {
  files = [...input.files].slice(0, MAX_FILES);
  grid.innerHTML = '';
  btnBar.innerHTML = '';
  detailBox.innerHTML = '<p>Nie wybrano obrazu.</p>';
  store.length = 0;

  files.forEach((file, i) => {
    const wrap = document.createElement('div');
    wrap.className = 'img-wrap';

    const img = document.createElement('img');
    img.id    = `img-${i}`;
    img.dataset.idx = i;                      // ← identyfikator dla RO
    img.src   = URL.createObjectURL(file);
    img.onload= () => {
      URL.revokeObjectURL(img.src);
      ro.observe(img);                        // ← obserwujemy rozmiar
    };

    const cvs = document.createElement('canvas');
    cvs.id    = `cvs-${i}`;

    wrap.appendChild(img);
    wrap.appendChild(cvs);
    grid.appendChild(wrap);
  });
});

/* ---------- ROZPOCZNIJ DETEKCJE ---------- */
runBtn.addEventListener('click', async () => {
  if (!files.length) return alert('Najpierw wybierz pliki.');

  btnBar.textContent = 'Przetwarzanie…';

  for (let i = 0; i < files.length; i++) {
    const fd = new FormData();
    fd.append('file', files[i]);

    let dets = [];
    try {
      const r = await fetch(API_URL, { method: 'POST', body: fd });
      if (r.ok) dets = (await r.json()).detections;
    } catch (e) { console.error(e); }

    const uniq = [...new Set(dets.map(d => d.label))];
    store[i] = { detections: dets, unique: uniq, fileName: files[i].name };

    drawBoxes(i, dets);                       // pierwszy rzut ramek
  }
  buildBtnBar();
});

/* ---------- RYSOWANIE RAMEK ---------- */
function drawBoxes(i, dets) {
  const img = document.getElementById(`img-${i}`);
  const cvs = document.getElementById(`cvs-${i}`);

  if (!img.complete || img.clientHeight === 0) {
    requestAnimationFrame(() => drawBoxes(i, dets));
    return;
  }

  cvs.width  = img.clientWidth;
  cvs.height = img.clientHeight;
  const ctx  = cvs.getContext('2d');
  ctx.clearRect(0, 0, cvs.width, cvs.height);

  const sx = cvs.width  / img.naturalWidth;
  const sy = cvs.height / img.naturalHeight;

  ctx.strokeStyle = '#ffbd39';
  ctx.lineWidth   = 2;
  ctx.font        = '14px Poppins';
  ctx.fillStyle   = '#000';
  ctx.strokeStyle = '#ffbd39';
  ctx.lineWidth   = 3;

  dets.forEach(d => {
    const [x1, y1, x2, y2] = d.bbox;
    ctx.strokeRect(x1 * sx, y1 * sy, (x2 - x1) * sx, (y2 - y1) * sy);
    ctx.strokeText(d.label, x1 * sx + 4, y1 * sy + 15);
    ctx.fillText  (d.label, x1 * sx + 3, y1 * sy + 15);
  });
}

/* ---------- PRZYCISKI OBRAZÓW ---------- */
function buildBtnBar() {
  btnBar.innerHTML = '';
  store.forEach((rec, i) => {
    const b = document.createElement('button');
    b.className = 'thumb-btn';
    b.dataset.idx = i;
    b.textContent = `Obraz ${i + 1} (${rec.detections.length})`;
    b.onclick = selectImg;
    btnBar.appendChild(b);
  });
  btnBar.firstChild && btnBar.firstChild.click();
}

/* ---------- PANEL SZCZEGÓŁÓW ---------- */
function selectImg(e) {
  [...btnBar.children].forEach(b => b.classList.remove('active'));
  e.currentTarget.classList.add('active');

  const i = +e.currentTarget.dataset.idx;
  const { fileName, detections, unique } = store[i];

  const desc = {
    /* --- A – znaki ostrzegawcze --- */
    'A-1':  'Niebezpieczny zakręt w prawo',
    'A-2':  'Niebezpieczny zakręt w lewo',
    'A-3':  'Niebezpieczne zakręty, pierwszy w prawo',
    'A-4':  'Niebezpieczne zakręty, pierwszy w lewo',
    'A-5':  'Skrzyżowanie dróg',
    'A-6a': 'Skrzyżowanie z drogą podporządkowaną z prawej',
    'A-6b': 'Skrzyżowanie z drogą podporządkowaną z lewej',
    'A-6c': 'Skrzyżowanie z drogą podporządkowaną po obu stronach',
    'A-7':  'Ustąp pierwszeństwa',
    'A-8':  'Skrzyżowanie o ruchu okrężnym',
    'A-9':  'Przejazd kolejowy z zaporami',
    'A-10': 'Przejazd kolejowy bez zapór',
    'A-11': 'Nierówna droga',
    'A-12': 'Próg zwalniający',
    'A-16': 'Przejście dla pieszych',
    'A-17': 'Dzieci',
    'A-18a':'Zwierzęta gospodarskie',
    'A-18b':'Zwierzęta dzikie',
    'A-20': 'Odcinek jezdni o ruchu dwukierunkowym',
    'A-21': 'Przejazd przez tory tramwajowe',
  
    /* --- B – zakazy --- */
    'B-1':  'Zakaz ruchu w obu kierunkach',
    'B-2':  'Zakaz wjazdu',
    'B-3':  'Zakaz wjazdu pojazdów silnikowych',
    'B-9':  'Zakaz wjazdu rowerów',
    'B-20': 'Stop',
    'B-21': 'Zakaz skrętu w lewo',
    'B-22': 'Zakaz skrętu w prawo',
    'B-24': 'Zakaz zawracania',
    'B-33': 'Ograniczenie prędkości',
    'B-36': 'Zakaz zatrzymywania',
    'B-38': 'Zakaz postoju',
  
    /* --- C – nakazy --- */
    'C-1':  'Nakaz jazdy na wprost',
    'C-2':  'Nakaz skrętu w prawo',
    'C-3':  'Nakaz skrętu w lewo',
    'C-4':  'Nakaz jazdy prosto lub w prawo',
    'C-5':  'Nakaz jazdy prosto lub w lewo',
    'C-6':  'Nakaz jazdy w prawo lub w lewo',
    'C-9':  'Nakaz jazdy z prawej strony znaku',
    'C-10': 'Nakaz jazdy z lewej strony znaku',
    'C-12': 'Ruch okrężny',
  
    /* --- D – informacyjne --- */
    'D-1':  'Droga z pierwszeństwem',
    'D-2':  'Koniec drogi z pierwszeństwem',
    'D-3':  'Droga jednokierunkowa',
    'D-6':  'Przejście dla pieszych',
    'D-6a': 'Przejazd dla rowerzystów',
    'D-6b': 'Przejście i przejazd dla rowerzystów',
    'D-8':  'Droga ekspresowa',
    'D-9':  'Koniec drogi ekspresowej',
    'D-12': 'Pas ruchu dla autobusów',
    'D-15': 'Początek autostrady',
    'D-16': 'Koniec autostrady',
    'D-18': 'Parking',
  };

  detailBox.innerHTML = `
    <p><strong>${fileName}</strong></p>
    <p>Wykryto <strong>${detections.length}</strong> znak(i).</p>
    <p>Etykiety:</p>
    <ul>
      ${unique.map(l => `<li><strong>${l}</strong> – ${desc[l] || 'opis nieznany'}</li>`).join('')}
    </ul>
  `;
}
