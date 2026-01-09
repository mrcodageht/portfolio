export function log(type, msg, src) {
  console.log(`==> [${src}] [${type}] - ${msg}`);
}

export function logObj(type, obj, msg = "", src="") {
  console.table(`==> [${src}] [${type}] - ${msg}`, obj);
}

export const TYPE = {
  DEBUG: "DEBUG",
  INFO: "INFO",
};
