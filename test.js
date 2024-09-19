
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

let encoded_string = "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";
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



