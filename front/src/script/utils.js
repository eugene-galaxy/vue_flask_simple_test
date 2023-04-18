const API_URL = "http://localhost:20230/";

export function formToJson(form) {
  const res = {};
  for (const element of form.elements) {
    if (element.tagName === "BUTTON") continue;
    if (element.type === "checkbox") {
      res[element.name] = element.checked;
    } else if (element.type === "number") {
      res[element.name] = Number(element.value);
    } else if (element.value?.length) {
      res[element.name] = element.value;
    }
  }
  return res;
}

export async function api(endpoint, data = null) {
  const res = await fetch(API_URL + endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return await res.json();
}
