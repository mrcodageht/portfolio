export function log(type, msg) {
  console.log(`==> [${type}] - ${msg}`);
}

export function logObj(type, obj, msg = "") {
  console.table(`==> [${type}] - ${msg}`, obj);
}

export const TYPE = {
  DEBUG: "DEBUG",
  INFO: "INFO",
};
