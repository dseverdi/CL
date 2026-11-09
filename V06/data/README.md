# Korpus

Rečenice iz treebanka **UD Croatian SET** (Universal Dependencies) s oznakom izvora.

* `set_train.tsv` (6914 rečenica), `set_dev.tsv` (960), `set_test.tsv` (1036; bez 100 rečenica s Wikipedije, kojih nema u skupu za učenje).
* Stupci odvojeni tabulatorom: izvor (`set` = SETimes, `news` = hrvatski portal, `web` = hrvatski web), rečenica.
* Izvor je preuzet iz oznake rečenice (`# sent_id`) u datotekama `hr_set-ud-*.conllu`.

Izvor: https://github.com/UniversalDependencies/UD_Croatian-SET
Licencija: CC BY-SA 4.0 (vidi `LICENSE.txt`)

Recenzije filmova (5. dio) preuzima NLTK: `nltk.download("movie_reviews")`.
