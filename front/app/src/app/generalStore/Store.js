import { combineReducers, createStore, applyMiddleware } from 'redux'

import thunk  from 'redux-thunk'
import logger from 'redux-logger'

import { products, initialState as productsStore } from '../reducers/products'

import { cart, initialState as cartStore } from '../reducers/cart'

// Combine all reducers
const reducers = combineReducers({
    products,
    cart
})

// Create a middleware to wraps an data to delay its evaluation
const middlewares = [thunk]

if (process.env.NODE_ENV !== 'production') {
    middlewares.push(logger)
}

// Apply middelwares
const enhancer = applyMiddleware(...middlewares)

// Define Global Store
const GlobalStore = {
						products: productsStore,
						cart: cartStore
					}

// Create the Store
let Store = createStore(reducers, GlobalStore, enhancer)

export default Store