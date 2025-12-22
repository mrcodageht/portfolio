export function log(type, msg) {
  console.log(`==> [${type}] - ${msg}`)
}

export function logObj(type, msg) {
  console.table(`==> [${type}] - `, msg)
}


export const TYPE = {
  DEBUG: 'DEBUG',
  INFO: 'INFO'
};