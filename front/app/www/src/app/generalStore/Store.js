import { combineReducers, createStore, applyMiddleware } from 'redux'

import thunk  from 'redux-thunk'
import logger from 'redux-logger'
import createHistory from 'history/createBrowserHistory'
import { routerReducer, routerMiddleware } from 'react-router-redux'


import { products, initialState as productsStore } from '../reducers/products'

import { session, initialState as sessionStore } from '../reducers/session'

import { cart, initialState as cartStore } from '../reducers/cart'

// Create a history of your choosing (we're using a browser history in this case)
export const history = createHistory()

// Combine all reducers
const reducers = combineReducers({
  products,
  cart,
  session,
  router: routerReducer
})

// Create a middleware to wraps an data to delay its evaluation
const middlewares = [thunk, routerMiddleware(history)]

if (process.env.NODE_ENV !== 'production') {
  middlewares.push(logger)
}

// Apply middelwares
const enhancer = applyMiddleware(...middlewares)

// Define Global Store
const GlobalStore = {
  session: sessionStore,
  products: productsStore,
  cart: cartStore
}

// Create the Store
export let Store = createStore(reducers, GlobalStore, enhancer)

