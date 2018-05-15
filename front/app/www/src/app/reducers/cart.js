import {
	ADD_TO_CART,
	REMOVE_TO_CART,
	PAYD
} from '../actions/cart'

export const CART_NOT_LOADED = 0
export const CART_LOADING    = 1
export const CART_LOADED     = 2

// Defined a default state
export const initialState = {
	items: [],
    totalPrice:0
}

export function cart(state = initialState, action) {
    switch (action.type) {
        case ADD_TO_CART:
            state.items.push(action.data)
            state.totalPrice += action.data.price
        	return Object.assign({}, state)

        case REMOVE_TO_CART:
            state.items.splice(action.data, 1)
            let price = 0
            for(let item of state.items) {
                price += item.price
            }
            state.totalPrice = price
        	return Object.assign({}, state)

        case PAYD:
	        return Object.assign({}, state, {
                cart: action.data.cart
            })
        default:
            return state
    }
}