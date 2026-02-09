/* =========================================================
 * Holiday definitions (Lunar)
 * ========================================================= */

const HOLIDAYS = [
  { name: "Tết Nguyên Đán", d: 1, m: 1 },
  { name: "Rằm tháng Giêng", d: 15, m: 1 },
  { name: "Giỗ Tổ Hùng Vương", d: 10, m: 3 },
  { name: "Phật Đản", d: 15, m: 4 },
  { name: "Lễ Đoan Ngọ", d: 5, m: 5 },
  { name: "Vu Lan", d: 15, m: 7 },
  { name: "Tết Trung Thu", d: 15, m: 8 },
  // 👇 IMPORTANT
  { name: "Ông Táo chầu trời", d: 23, m: 12, nextSolarYear: true }
];

/* =========================================================
 * Solar → Lunar (USING HND ENGINE)
 * ========================================================= */

function solarToLunar(dd, mm, yy) {
  return getLunarDate(dd, mm, yy);
}

function pad2(n) {
  return n < 10 ? "0" + n : String(n);
}


/* =========================================================
 * Find holiday in a given Lunar year
 * ========================================================= */

function findHoliday(lunarYear, h) {
  const solarYear = h.nextSolarYear ? lunarYear + 1 : lunarYear;

  for (let m = 1; m <= 12; m++) {
    for (let d = 1; d <= 31; d++) {
      try {
        const lunar = getLunarDate(d, m, solarYear);
        if (
          lunar.day === h.d &&
          lunar.month === h.m &&
          lunar.leap === 0 &&
          lunar.year === lunarYear
        ) {
          return `${pad2(d)}/${pad2(m)}/${solarYear}`;
        }
      } catch {
        continue;
      }
    }
  }
  return "—";
}

/* =========================================================
 * Can–Chi helpers (HND-native)
 * ========================================================= */

function canChiYear(year) {
  return getYearCanChi(year);
}

/* =========================================================
 * HTML Table Generator (2021–2035 optimized)
 * ========================================================= */

function generate_table() {
  const startYear = parseInt(document.getElementById("startYear").value);
  const endYear = startYear + 9;

  // Set title
  document.getElementById("calendarTitle").innerHTML =
    `<h2>Bảng các ngày lễ âm lịch quan trọng cho 10 năm: ${startYear} - ${endYear}</h2>`;

  // Define holidays
  const holidays = [
    { name: "Tết Nguyên Đán", d: 1, m: 1 },
    { name: "Rằm tháng Giêng", d: 15, m: 1 },
    { name: "Giỗ Tổ Hùng Vương", d: 10, m: 3 },
    { name: "Phật Đản", d: 15, m: 4 },
    { name: "Lễ Đoan Ngọ", d: 5, m: 5 },
    { name: "Vu Lan", d: 15, m: 7 },
    { name: "Tết Trung Thu", d: 15, m: 8 },
    { name: "Ông Táo chầu trời", d: 23, m: 12, nextSolarYear: true } // next year
  ];

  // Create table header
  let tableHTML = `<table border="1" cellpadding="5" cellspacing="1"><tr><td>Ngày lễ</td>`;
  for (let y = startYear; y <= endYear; y++) {
    tableHTML += `<th>${getYearCanChi(y)}<br>${y}</th>`;
  }
  tableHTML += "</tr>";

  // Fill table rows
  for (let h of holidays) {
    tableHTML += `<tr><td><b>${h.name}</b></td>`;
    for (let y = startYear; y <= endYear; y++) {
      const dateStr = findHoliday(y, h); // use padded & Ông Táo logic
      tableHTML += `<td>${dateStr}</td>`;
    }
    tableHTML += "</tr>";
  }

  tableHTML += "</table>";

  document.getElementById("holidayTable").innerHTML = tableHTML;
}


/* =========================================================
 * Form handler
 * ========================================================= */

function handleFormSubmit(e) {
  e.preventDefault();
  const y = parseInt(e.target.yy.value, 10);
  if (!isNaN(y)) generate_table(y);
}
