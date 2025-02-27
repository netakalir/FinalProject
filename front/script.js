let serverStatus = "The server is offline";
/*שורה זו יוצרת משתנה בשם מצב שרת ו מקצה לו ערך מסויים.
 משתנה זה ישמש בהמשך הקוד לאחסן ולעדכן את מצב החיבור לשרת.*/


const privateIds = new WeakMap();

class IdList {
    constructor(ids) {
        privateIds.set(this, {
            ids: ids
        });
    }
    getIds() {
        return privateIds.get(this).ids;
    }
}


async function fetchLogs() {
    try {
        const response = await fetch('http://127.0.0.1:5000/logs_list');
        if (response.ok) {
            const data = await response.json();
            displayLogs(data.logs);
            serverStatus = "The server sent information";
        } else if (response.status === 404) {
            displayError('השרת לא מצא את המשאב המבוקש.');
        } else if (response.status === 500) {
            displayError('שגיאת שרת פנימית.');
        } else {
            displayError('שגיאה לא ידועה בשרת.');
        }
    } catch (error) {
        console.error("Error fetching logs:", error);
        displayError('The server is unavailable.');
        serverStatus = "The server is offline";
    }
    updateStatus();
}
/* פונקציה זו שולחת בקשה לשרת, מטפלת בתגובה.
מעדכנת את מצב החיבור לשרת ומציגה את הנתונים שהתקבלו*/


function displayLogs(logs){
    const logTable = document.getElementById('logTable');
    logTable.innerHTML = "";
    logs.forEach(log =>{
        const row = document.createElement('tr');
        row.innerHTML = `<td>${log.time}</td>
                         <td>${log.decrypted_data}</td>
                         <td>${formatSystemInfo(log.system)}</td>`;
        logTable.appendChild(row);
    });
}
/* הפונקציה מקבלת מערך של רשומות יומן ועושה כמה פעולות
1 מנקה את תוכן הטבלה
2יוצרת שורה חדשה בטבלה עבור כל רשומה ביומן
כל שורה ביומן תכיל את זמן הרשומה ,הנתונים המפוענחים ומידע על המערכת*/


function formatSystemInfo(system){
    let formattedSystemInfo = "";
    for (const [key, value] of Object.entries(system)){
        formattedSystemInfo += `${key}: ${value}<br>`;
    }
    return formattedSystemInfo;
}
/*הפונקציה מקבלת אוביקט שמכיל מידע על המערכת.
הפונקציה תחזיר מחרוזת html
שתציג את המידע בצורת קריאה עם שבירת שורה בין כל מאפיין וערך
המחרוזת הזו יכולה בסוף להיות מוצגת בדף html */


function searchLogs(){
    let searchText = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.getElementById('logTable').children;
    for (let row of rows) {
        row.style.display = 'table-row';
        let found = false;
        row.querySelectorAll('td').forEach(cell => {
            cell.innerHTML = cell.innerHTML.replace(/<span class="highlight">(.*?)<\/span>/g, '$1');
            if (cell.innerText.toLowerCase().includes(searchText) && searchText !== "") {
                found = true;
                cell.innerHTML = cell.innerHTML.replace(new RegExp(searchText, 'gi'), match => `<span class="highlight">${match}</span>`);
            }
        });
        if (!found && searchText !== "") {
            row.style.display = 'none';
        }
    }
}
/*הפונקציה מאפשרת למשתמ לחפש טקסט בטבלה
מתבצע מעבר על שורה ועל כל תא
מתבצעת בדיקהת התאמה והדגשת תוצאות החיפוש 
תתבצע הסתרה של שורות ותאים לא רלוונטיים
הפונקציה גם תסיר הדגשות קודמות לפני ביצוע החיפוש החדש */


function updateStatus(){
    const statusElement = document.getElementById('status');
    statusElement.innerText = serverStatus;
}
/* הפונקציה מאתרת אלמנט עם מזהה יחודי 
מעדכנת את תוכן הטקסט שלו לערך המשתנה מצב השרת 
פונקציה משמשת לעדכון דינמי של המצב בדף ה html*/


async function openFileNamesPage(){
    try {
     const response = await fetch('http://127.0.0.1:5000/get_file_name');
     if (response.ok) {
       const files = await response.json();
       let htmlContent = `<h1>שמות קבצים</h1>`;
       htmlContent += `</div><br><button onclick="goBackToMainPage()">חזור לדף הראשי</button>`;
       htmlContent += `<input type="text" id="fileSearch" placeholder="חפש שם קובץ" oninput="searchFileNames()">`;
       htmlContent += `<div id="fileNamesContainer">`;
       files.forEach(file => {
        //  htmlContent += `<div><button onclick="openFileContent('${file}')">${file}</button></div>`;
         htmlContent += `<div style="cursor: pointer;" onclick="openFileContent('${file}')">${file}</div>`;
         
       });
       document.body.innerHTML = htmlContent;
     } else {
       alert("שגיאה בקבלת שמות הקבצים");
     }
   } catch (error) {
     console.error("Error in openFileNamesPage:", error);
     displayError(("שגיאה בטעינת שמות הקבצים: " + error));
   }
}
/* הפונקציה מאחזרת רשימת שמות קבצים מהשרת
יוצרת דף html דינמי להצגתם
הפונקציה כוללת טיפול בשגיאות ומאפשרת למשתמש לחזור לדף הראשי ולחפש שמות קבצים אחרים*/


function searchFileNames(){
    let searchText = document.getElementById('fileSearch').value.toLowerCase();
    const fileButtons = document.querySelectorAll('#fileNamesContainer button');
    fileButtons.forEach(button => {
        if (button.innerText.toLowerCase().includes(searchText)) {
            button.style.display = 'block';
        } else {
            button.style.display = 'none';
        }
    });
}
/* הפונקציה מאפשרת למשתמש לחפש שמות קבצים
הפונקציה מקבלת טקסט לחיפוש 
עוברת על כל כפתור שמציג שם קובץ ובודקת האם הקובץ הזה מכיל את הטקסט שמחפשים
אם כן אז הכפתור יוצג אחרת הוא יוסתר
זה מאפשר למשתמש לסנן את הקבצים בקלות*/


async function openFileContent(file) {
    let fixedFilename = file.endsWith('.txt') ? file : file + '.txt';
    try {
        const response = await fetch('http://127.0.0.1:5000/get_by_name/' + fixedFilename);
        if (response.ok) {
            const data = await response.text();
            displayFileContent(file, data);
        } else {
            displayError("הקובץ לא נמצא");
        }
    } catch (error) {
        displayError("שגיאה בעת בקשת תוכן הקובץ: " + error);
    }
}

function displayFileContent(file, data) {
    let entries = data.trim().split(/\r?\n\r?\n/);
    let tableHtml = `<h2>תוכן הקובץ ${file}</h2>`;
    tableHtml += `<button onclick="goBackToFileNamesPage()">חזור לשמות קבצים</button>`;
    tableHtml += `<button onclick="printFileContent()">הדפס תוכן</button>`;
    tableHtml += `<input type="text" id="searchInFile" placeholder="חפש במידע" oninput="searchInFileContent()">`;
    tableHtml += `<table><thead><tr><th>זמן</th><th>מידע</th><th>מערכת</th></tr></thead><tbody>`;
    entries.forEach(entry => {
        const rowHtml = createFileTableRow(entry);
        tableHtml += rowHtml;
    });
    tableHtml += '</tbody></table>';
    document.body.innerHTML = tableHtml;
}

function createFileTableRow(entry) {
    const lines = entry.split(/\r?\n/).filter(line => line.trim() !== "");
    if (lines.length >= 3) {
        let time = lines[0].replace("Time:", "").trim();
        let decryptedData = lines[1].replace("Decrypted Data:", "").trim();
        let systemInfoFormatted = formatSystemInfo(lines[2].replace("System Info:", "").trim());
        return `<tr><td>${time}</td><td>${decryptedData}</td><td>${systemInfoFormatted}</td></tr>`;
    }
    return '';
}

function formatSystemInfo(systemInfoStr) {
    let systemInfoFormatted = "";
    try {
        for (const [key, value] of Object.entries(systemInfoStr)) {
            systemInfoFormatted += `${key}: ${value}<br>`;
        }
    }catch (e) {
        console.error("Error parsing JSON:", e);
        systemInfoFormatted = "פורמט מידע מערכת לא תקין.";
    }
    return systemInfoFormatted;
}


function searchInFileContent(){
    let searchText = document.getElementById('searchInFile').value.toLowerCase();
    const rows = document.querySelectorAll('table tr');
    rows.forEach(row => {
        row.style.display = 'table-row';
        let found = false;
        row.querySelectorAll('td').forEach(cell => {
            cell.innerHTML = cell.innerHTML.replace(/<span class="highlight">(.*?)<\/span>/g, '$1');
            if (cell.innerText.toLowerCase().includes(searchText) && searchText !== "") {
                found = true;
                cell.innerHTML = cell.innerHTML.replace(new RegExp(searchText, 'gi'), match => `<span class="highlight">${match}</span>`);
            }
        });
        if (!found && searchText !== "") {
            row.style.display = 'none';
        }
    });
}
/* הפונקציה מאפשרת למשתמ לחפש טקסט בטבלה
מתבצע מעבר על שורה ועל כל תא
מתבצעת בדיקהת התאמה והדגשת תוצאות החיפוש 
תתבצע הסתרה של שורות ותאים לא רלוונטיים
הפונקציה גם תסיר הדגשות קודמות לפני ביצוע החיפוש החדש 
 ההבדל בינה לבין function searchLogs
 הוא מה המטרה שלך חיפוש בטבלה אחת מוך מספר טבלאות אז תשתמש ב function searchLogs
 אבל אם אתה רוצה לחפש מידע בכל הטבלאות אז תשתמש ב searchInFileCo */


function goBackToFileNamesPage(){
    openFileNamesPage();
}
//הפונקציה משמשת כלי לניווט המשתמש חזרה לדף של רשימת הקבצים


function goBackToMainPage(){
    location.reload();
}
//הפונקציה תגרום לדפדפן לטעון מחדש את הדף הנוכחי בדומה לכפתור רענן 


function printFileContent(){
    window.print();
}
//הפונקציה תציג את דיאלוג ההדפסה ותאפשר למשתמש להדפיס את הדף הנוכחי


window.addEventListener("load", () =>{
    fetchLogs();
    setInterval(fetchLogs, 1000 * 60);
});
/* כאשר הדף יטען במלואו תתבצע קריאה בפעם הראשונה לפנקציה fetchLogs
לאחר מכן יוגדר מרווח זמן שפה הוא מוגדר לחמש שניות ובכל סיום מרווח הזמן תתבצע הקריאה ל fetchLogs*/


async function loadValidIds() {
    const response = await fetch('validIds.json');
    if (response.ok) {
        return await response.json();
    } else {
        console.error('Failed to load valid IDs.');
        return [];
    }
}
/*הפונקציה מבצעת קריאה לשרת ומביאה את רשימת המזהים המורשים
הפונקציה מחזירה את המידע שהתקבל מהשרת*/


async function validateCredentials() {
    const idNumber = document.getElementById("id-number").value;
    const passwordInput = document.getElementById("password").value;
    const validIds = await loadValidIds();
    const validPasswords = await loadValidPasswords();

    if (!checkID(idNumber)) {
        displayError("מספר זהות לא תקין.");
        return;
    }

    if (!validIds.includes(idNumber)) {
        displayError("מספר זהות שגוי.");
        return;
    }

    if (!validPasswords.includes(passwordInput)) {
        displayError("סיסמה שגויה.");
        return;
    }
    
    // אימות הצליח - הפניה לדף הראשי
    window.location.href = "index.html";
}

async function loadValidIds() {
    try {
        const response = await fetch("validids.json");
        const data = await response.json();
        return data.validlds;
    } catch (error) {
        console.error("שגיאה בטעינת תעודות זהות:", error);
        return [];
    }
}

async function loadValidPasswords() {
    try {
        const response = await fetch("password.json");
        const data = await response.json();
        return data.password;
    } catch (error) {
        console.error("שגיאה בטעינת סיסמאות:", error);
        return [];
    }
}

function checkID(id) {
    return /^\d{9}$/.test(id);
}

function displayError(message) {
    const errorMessage = document.getElementById("error-message");
    errorMessage.textContent = message;
}


function updateCountdown() {
    const targetDate = new Date("2023-10-07T06:30:00Z");
    const currentDate = new Date();
    const timeDifference = Math.floor((currentDate - targetDate) / 1000);

    const days = Math.floor(timeDifference / (60 * 60 * 24));
    const hours = Math.floor((timeDifference % (60 * 60 * 24)) / (60 * 60));
    const minutes = Math.floor((timeDifference % (60 * 60)) / 60);
    const seconds = timeDifference % 60;

    document.getElementById("days").textContent = days.toString().padStart(3, '0');
    document.getElementById("hours").textContent = hours.toString().padStart(2, '0');
    document.getElementById("minutes").textContent = minutes.toString().padStart(2, '0');
    document.getElementById("seconds").textContent = seconds.toString().padStart(2, '0');
}

setInterval(updateCountdown, 1000);
  
