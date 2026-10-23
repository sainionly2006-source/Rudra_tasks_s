# Task 5 — Synthetic Sensor Data Schema

## Objective
Define a consistent JSON structure for simulated robotics sensor messages. This task uses synthetic data only and does not require physical hardware.

## Required fields
- `timestamp`: a non-empty ISO-8601 date/time string, for example `2026-10-24T10:00:00Z`.
- `sensor_id`: a non-empty identifier for the sensor, for example `TEMP-001`.
- `value`: a numeric measurement, for example `24.5`.
- `unit`: a non-empty measurement unit, for example `C` or `kPa`.
- `status`: one of `ok`, `warning`, or `error`.

Unknown extra fields are not allowed by this schema.

## Example valid message
```json
{
  "timestamp": "2026-10-24T10:00:00Z",
  "sensor_id": "TEMP-001",
  "value": 24.5,
  "unit": "C",
  "status": "ok"
}
```

## How to verify on Windows
1. Open `M05_Synthetic_Sensor_Schema.json` in VS Code.
2. Confirm that the file is valid JSON and that all five required fields are present.
3. If you have already downloaded the complete RudraEdge package, open a terminal in `RudraEdge_Software_Package` and run:
   `python -m unittest discover -s tests -v`
4. Keep the actual terminal output or a screenshot as evidence. Do not claim a test passed unless you ran it.

## Git upload
Place this folder inside your existing `Rudra` project/repository, then commit and push the two files. See the Hindi instructions in the chat for the Git steps.
                            Detailed Information
# Task 5 — Synthetic Sensor Data Schema

## 1. Task का नाम
**Synthetic Sensor Data Schema (सिंथेटिक सेंसर डेटा स्कीमा)**

## 2. Objective (उद्देश्य)
इस task का मुख्य उद्देश्य simulated robotics sensors से मिलने वाले data के लिए एक standard JSON structure बनाना है। इससे sensor messages को एक निश्चित format में store, read और validate किया जा सकता है।

यह project software simulation और synthetic data पर आधारित है। इसमें किसी physical sensor या robot hardware की आवश्यकता नहीं है।

## 3. Project File
इस task की मुख्य file है:

`M05_Synthetic_Sensor_Schema.json`

यह file sensor message में आवश्यक fields, उनके data types और allowed values को define करती है।

## 4. Sensor Data Fields

एक sensor message में निम्नलिखित पाँच fields आवश्यक हैं:

| Field | Data Type | Description |
|---|---|---|
| `timestamp` | String | Sensor reading का date और time |
| `sensor_id` | String | Sensor की unique पहचान |
| `value` | Number | Sensor द्वारा मापी गई value |
| `unit` | String | Measurement की unit |
| `status` | String | Reading की स्थिति |

### Field Details

**1. timestamp**

यह बताता है कि sensor reading कब generate हुई। उदाहरण: `2026-10-24T10:00:00Z`। JSON Schema इसे string के रूप में define करती है; वास्तविक timestamp validation parser में भी की जाती है।

**2. sensor_id**

यह sensor की पहचान के लिए उपयोग होता है। उदाहरण: `TEMP-001` या `PRESS-002`।

**3. value**

यह sensor की numerical reading होती है। उदाहरण: `24.5` या `101.2`।

**4. unit**

यह reading की measurement unit बताता है। उदाहरण: `C` (Celsius) या `kPa` (kilopascal)।

**5. status**

यह reading की स्थिति बताता है। इस project में तीन values allowed हैं:

- `ok` — Reading सामान्य है।
- `warning` — Reading पर ध्यान देने की आवश्यकता हो सकती है।
- `error` — Reading या sensor स्थिति में error दर्शाया गया है।

## 5. Example of Synthetic Sensor Message

नीचे एक valid-format sensor message का उदाहरण है:

```json
{
  "timestamp": "2026-10-24T10:00:00Z",
  "sensor_id": "TEMP-001",
  "value": 24.5,
  "unit": "C",
  "status": "ok"
}
```

यह उदाहरण temperature sensor की simulated reading दर्शाता है।

## 6. Data Validation Rules

इस task में निम्नलिखित नियम निर्धारित किए गए हैं:

1. सभी पाँच required fields मौजूद होनी चाहिए।
2. `timestamp`, `sensor_id` और `unit` non-empty strings होने चाहिए।
3. `value` numerical होना चाहिए।
4. `status` केवल `ok`, `warning` या `error` हो सकता है।
5. अतिरिक्त, अनजान fields स्वीकार नहीं की जातीं।
6. Parser ISO-8601 timestamp format और finite numerical values की भी जाँच करता है।

## 7. Role of JSON Schema

JSON Schema sensor messages के structure और expected data types को define करती है। इससे developers को यह समझने में सहायता मिलती है कि data किस format में होना चाहिए।

इस project में Python parser अतिरिक्त runtime validation करता है। JSON Schema file अपने आप data validate नहीं करती; उसे किसी compatible validator या application द्वारा उपयोग किया जाना चाहिए।

## 8. Execution and Verification

Windows पर project verify करने के लिए:

1. VS Code में `Rudra_Software_Package` या अपने वास्तविक integrated project folder को खोलें।
2. Terminal खोलें।
3. Project root में यह command चलाएँ:

```bash
python -m unittest discover -s tests -v
```

4. Demo चलाने के लिए:

```bash
python -m src.demo
```

5. Terminal output देखकर वास्तविक verification result record करें।

ध्यान दें: ये commands तभी काम करेंगी जब `src` और `tests` वाले integrated project folders उपलब्ध हों।

## 9. Expected Outcome

इस task का expected outcome एक व्यवस्थित JSON Schema file है, जो synthetic sensor messages का standard structure define करती है।

इससे आगे के tasks में sensor data parsing, validation, error handling और automated testing करना आसान होता है।

## 10. Conclusion

Task 5 में synthetic sensor data के लिए एक standard message structure define किया गया है। इसमें timestamp, sensor identifier, numerical value, unit और status शामिल हैं।

यह schema आगे के software development tasks के लिए एक आधार तैयार करती है और robotics software में consistent data handling को support करती है।

## 11. Deliverables

- `M05_Synthetic_Sensor_Schema.json`
- `NOTES_HINDI.md`

दोनों files को Git repository में Task 5 के folder के अंतर्गत maintain किया जाना चाहिए।
