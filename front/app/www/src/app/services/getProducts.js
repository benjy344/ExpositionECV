import fetch from 'isomorphic-fetch'

export function getProducts() {
  return fetch( '../src/public/contrib/products.json' )
}
