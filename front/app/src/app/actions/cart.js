// ACTIONS
export const ADD_TO_CART    = 'ADD_TO_CART'
export const REMOVE_TO_CART = 'REMOVE_TO_CART'
export const PAYD           = 'PAYD'


export function addToCart( data ) {
    return function (dispatch) {
        dispatch({
            type: ADD_TO_CART,
            data: data
        })
    }
}

export function removeToCart( data ) {
    return function (dispatch) {
        dispatch({
            type: REMOVE_TO_CART,
            data: data
        })
    }
}