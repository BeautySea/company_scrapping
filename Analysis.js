var Xd = {
    transitional: {
        silentJSONParsing: !0,
        forcedJSONParsing: !0,
        clarifyTimeoutError: !1
    },
    adapter: CC(),
    transformRequest: [function(e, n) {
        return Ag(n, "Accept"),
        Ag(n, "Content-Type"),
        $n.isFormData(e) || $n.isArrayBuffer(e) || $n.isBuffer(e) || $n.isStream(e) || $n.isFile(e) || $n.isBlob(e) ? e : $n.isArrayBufferView(e) ? e.buffer : $n.isURLSearchParams(e) ? (Mg(n, "application/x-www-form-urlencoded;charset=utf-8"),
        e.toString()) : $n.isObject(e) || n && n["Content-Type"] === "application/json" ? (Mg(n, "application/json"),
        EC(e)) : e
    }
    ],
    transformResponse: [function(e) {
        var n = this.transitional
          , r = n && n.silentJSONParsing
          , a = n && n.forcedJSONParsing
          , s = !r && this.responseType === "json";
        if (s || a && $n.isString(e) && e.length)
            try {
                return JSON.parse(e)
            } catch (l) {
                if (s)
                    throw l.name === "SyntaxError" ? $C(l, this, "E_JSON_PARSE") : l
            }
        return e
    }
    ],
    timeout: 0,
    xsrfCookieName: "XSRF-TOKEN",
    xsrfHeaderName: "X-XSRF-TOKEN",
    maxContentLength: -1,
    maxBodyLength: -1,
    validateStatus: function(e) {
        return e >= 200 && e < 300
    }
};
Xd.headers = {
    common: {
        Accept: "application/json, text/plain, */*"
    }
};
$n.forEach(["delete", "get", "head"], function(e) {
    Xd.headers[e] = {}
});
$n.forEach(["post", "put", "patch"], function(e) {
    Xd.headers[e] = $n.merge(TC)
});
var sm = Xd, AC = or, MC = sm, OC = function(e, n, r) {
    var a = this || MC;
    return AC.forEach(r, function(l) {
        e = l.call(a, e, n)
    }),
    e
}, ef, Og;

var Lg = or
  , oE = ak
  , Nu = aE
  , uE = ck
  , dE = sm;
function gk(t) {
    var e = new Nu(t)
      , n = oE(Nu.prototype.request, e);
    return Lg.extend(n, Nu.prototype, e),
    Lg.extend(n, e),
    n
}
var Br = gk(dE);
Br.Axios = Nu;
Br.create = function(e) {
    return gk(uE(Br.defaults, e))
}
;
Br.Cancel = vk();
Br.CancelToken = sE();
Br.isCancel = dk();
Br.all = function(e) {
    return Promise.all(e)
}
;
Br.spread = lE();
Br.isAxiosError = iE();
nm.exports = Br;
nm.exports.default = Br;
var cE = nm.exports
  , fE = cE;
function X2(t) {
    return t && t.__esModule && Object.prototype.hasOwnProperty.call(t, "default") ? t.default : t
}
const KungPt = X2(fE);

const Pe = Lr("root", {
    state: () => ({
        aktivKungorelse: null,
        aktivUppgiftslamnare: null,
        aktivKungorelsetyp: null,
        savedKungorelse: null,
        ersattsAvKungorelse: null,
        senastKoppling: null,
        nyaKungorelser: [],
        kungorelsetyper: [],
        underrubriker: [],
        loadedKungorelse: null,
        loadedKungorelsetyp: null,
        loadedUnderrubrik: null,
        startsida: !1,
        fulvisa: !1,
        rensaSokHistorik: !1
    }),
    getters: {
        getAktivKungorelse: t => t.aktivKungorelse,
        getAktivUppgiftslamnare: t => t.aktivUppgiftslamnare,
        getAktivKungorelsetyp: t => t.aktivKungorelsetyp
    },
    actions: {
        async getKoppling() {
            const t = "/poit/rest/HamtaKoppling"
              , e = await Pt.get(t, {});
            return e.data != this.senastKoppling ? (this.senastKoppling = e.data,
            !0) : !1
        },
        async getKungorelse(t) {
            if (this.loadedKungorelse = null,
            this.ersattsAvKungorelse = null,
            navigator.webdriver == !0)
                throw fetch("/poit-app?l=92300254401", {
                    method: "HEAD",
                    cache: "no-cache"
                }),
                new Error("UNKNOWN");
            if (navigator.languages.length == 0)
                throw fetch("/poit-app?l=92300254402", {
                    method: "HEAD",
                    cache: "no-cache"
                }),
                new Error("UNKNOWN");
            if (window.document.documentElement.getAttribute("webdriver"))
                throw fetch("/poit-app?l=92300254403", {
                    method: "HEAD",
                    cache: "no-cache"
                }),
                new Error("UNKNOWN");
            for (const u in window)
                if (u.match(/^cdc_/ig))
                    throw fetch("/poit-app?l=92300254404", {
                        method: "HEAD",
                        cache: "no-cache"
                    }),
                    new Error("UNKNOWN");
            if ("_Selenium_IDE_Recorder"in window)
                throw fetch("/poit-app?l=92300254405", {
                    method: "HEAD",
                    cache: "no-cache"
                }),
                new Error("UNKNOWN");
            if ("__webdriver_script_fn"in document)
                throw fetch("/poit-app?l=92300254406", {
                    method: "HEAD",
                    cache: "no-cache"
                }),
                new Error("UNKNOWN");
            if (/HeadlessChrome/.test(window.navigator.userAgent))
                throw fetch("/poit-app?l=92300254407", {
                    method: "HEAD",
                    cache: "no-cache"
                }),
                new Error("UNKNOWN");
            const e = "/poit/rest/HamtaKungorelse?kungorelseid=" + t.kungorelseid + "&koppling=" + this.senastKoppling + "&version=4";
            let n = null;
            try {
                n = await KungPt.get(e, {})
            } catch (u) {
                throw new Error(u.response.status)
            }
            const r = qb(n.data);
            let a = Dp.Buffer.from(r, "base64");
            const s = new TextEncoder().encode(t.kungorelseid + this.senastKoppling)
              , l = await crypto.subtle.digest("SHA-256", s)
              , o = zb(a, new Uint8Array(l)).toString("utf8");
            if (this.loadedKungorelse = JSON.parse(o),
            this.loadedKungorelse.ersattsAv) {
                const u = "/poit/rest/HamtaKoppling";
                if ((await Pt.get(u, {})).data != this.senastKoppling)
                    throw Error;
                await new Promise(S => setTimeout(S, 250));
                const f = "/poit/rest/HamtaKungorelse?kungorelseid=" + this.loadedKungorelse.ersattsAv + "&koppling=" + this.senastKoppling + "&version=4";
                let p = null;
                try {
                    p = await Pt.get(f)
                } catch (S) {
                    if (S.response.status != "403")
                        throw new Error(S.response.status)
                }
                const h = qb(p.data);
                let v = Dp.Buffer.from(h, "base64");
                const y = new TextEncoder().encode(this.loadedKungorelse.ersattsAv + this.senastKoppling)
                  , k = await crypto.subtle.digest("SHA-256", y)
                  , $ = zb(v, new Uint8Array(k)).toString("utf8");
                this.ersattsAvKungorelse = JSON.parse($);
                const M = "/poit/rest/HamtaKungorelsetyp?externKod=" + this.ersattsAvKungorelse.rubrikExternKod;
                await Pt.get(M, {})
            }
        },
        async registreraKungorelser(t) {
            try {
                const e = dt().getKundanvandare
                  , n = {
                    email: e.email,
                    token: e.token,
                    kungorelser: t
                }
                  , r = "/poit/rest/RegistreraKungorelser";
                return (await Pt.post(r, n)).data
            } catch {
                return []
            }
        },
        async updateraKungorelse(t) {
            try {
                const e = "/poit/rest/UpdateraKungorelse"
                  , n = await Pt.post(e, t);
                return this.setSavedKungorelse(n.data),
                !0
            } catch {
                return !1
            }
        },
        async getKungorelsetyper(t) {
            try {
                const e = "/poit/rest/ListaKungorelseTyper?kundNummer=" + t
                  , n = await Pt.get(e, {});
                this.setKungorelsetyper(n.data)
            } catch {}
        },
        async getKungorelsetyp(t) {
            try {
                const e = "/poit/rest/HamtaKungorelsetyp?externKod=" + t
                  , n = await Pt.get(e, {});
                this.setLoadedKungorelsetyp(n.data)
            } catch {}
        },
        async getUnderrubriker(t) {
            try {
                const e = "/poit/rest/ListaUnderrubriker?rubrikExternKod=" + t
                  , n = await Pt.get(e, {});
                this.setUnderrubriker(n.data)
            } catch {}
        },
        async getUnderrubrik(t) {
            try {
                const e = "/poit/rest/HamtaUnderrubrik?externKod=" + t
                  , n = await Pt.get(e, {});
                this.setLoadedUnderrubrik(n.data)
            } catch {}
        },
        setRensaSokHistorik(t) {
            this.rensaSokHistorik = t
        },
        setAktivKungorelse(t) {
            this.aktivKungorelse = t
        },
        setAktivUppgiftslamnare(t) {
            this.aktivUppgiftslamnare = t
        },
        setAktivKungorelsetyp(t) {
            this.aktivKungorelsetyp = t
        },
        setKungorelsetyper(t) {
            t.sort( (e, n) => e.kungorelseRubrik < n.kungorelseRubrik ? -1 : 1),
            this.kungorelsetyper = t
        },
        setUnderrubriker(t) {
            t.sort( (e, n) => e.beskrivning < n.beskrivning ? -1 : 1),
            this.underrubriker = t
        },
        setLoadedKungorelsetyp(t) {
            this.loadedKungorelsetyp = t
        },
        setLoadedUnderrubrik(t) {
            this.loadedUnderrubrik = t
        },
        setSavedKungorelse(t) {
            this.savedKungorelse = t
        }
    }
})




