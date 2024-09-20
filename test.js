
//https://poit.bolagsverket.se/poit/rest/SokKungorelse?sokord=&kungorelseid=&kungorelseObjektPersonOrgnummer=&kungorelseObjektNamn=&tidsperiod=ANNAN_PERIOD&tidsperiodFrom=2024-09-17&tidsperiodTom=2024-09-17&amnesomradeId=2&kungorelsetypId=4&underRubrikId=6


//Key1_url = "https://poit.bolagsverket.se/poit/rest/HamtaKoppling"



// https://poit.bolagsverket.se/poit/rest/HamtaKungorelse?kungorelseid=K643060/24&koppling=K3757747159816565219&version=4

// https://poit.bolagsverket.se/poit/rest/HamtaKungorelsetyp?externKod=ABREG


const crypto = require("node:crypto")
function qb(t) {
  let e = "";
  for (let n = 0; n < t.length; n++)
      if (t.charCodeAt(n) >= 48 && t.charCodeAt(n) <= 57) {
          let r = t.charCodeAt(n) - 48;
          r = (r + 5) % 10,
          e += String.fromCharCode(r + 48)
      } else
          t.charAt(n) == t.charAt(n).toUpperCase() ? e += t.charAt(n).toLowerCase() : e += t.charAt(n).toUpperCase();
  return e
}

function zb(t, e) {
  for (let n = 0; n < t.length; n++)
      t[n] ^= e[n & 31] + (e[n + 8 & 31] ^ e[n + 17 & 31]),
      e[n & 31] += e[n + 3 & 31] ^ e[n + 7 & 31],
      e[n & 31] ^= e[n + 12 & 31] + e[n + 18 & 31];
  return t
}

let encoded_string = "!22/zgpkyysDoexGNqCTKvztmDanZa5rH8uYn9iuWQilwKiZdOpdD6wTZ4IYKqwp+UJwNclmvbvdsUcg="
let r = qb(encoded_string)
let a = Buffer.from(r, "base64");
const s = new TextEncoder().encode("K643060/24" + "K3757747159816565219")
async function getdata(){
    const l = await crypto.subtle.digest("SHA-256", s);
    const o = zb(a, new Uint8Array(l)).toString("utf8");
    const d =  JSON.parse(o);
    console.log(d)
}


getdata()

// str = decodeURIComponent("BOL_LB=!22/zgpkyysDoexGNqCTKvztmDanZa5rH8uYn9iuWQilwKiZdOpdD6wTZ4IYKqwp+UJwNclmvbvdsUcg=; path=/; Httponly; Secure");
// console.log("decodedURI=",str);


