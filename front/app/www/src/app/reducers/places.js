import {
    FETCH_PLACES,
    RECEIVE_PLACES,
    UPDATE_PLACES
} from '../actions/places'

// Defined Loading state
export const PLACES_NOT_LOADED = 0
export const PLACES_LOADING    = 1
export const PLACES_LOADED     = 2

// Defined a default state
export const initialState = {
    placesCount: 0,
    itemLoadState: 0,
    items: []
}

export function places(state = initialState, action) {
    switch (action.type) {
        case FETCH_PLACES:
            return Object.assign({}, state, {
                itemLoadState: PLACES_LOADING
            })

        case RECEIVE_PLACES:
            return Object.assign({}, state, {
                itemCount: action.data.items.length,
                itemLoadState: PLACES_LOADED,
                items: action.data.items
            })

        case UPDATE_PLACES:
            const tempItems = state.items.map(item => {
                if (item.id === action.data.id) {
                    item.available = true
                }
                return item
            })
            return Object.assign({}, state, {items:tempItems})

        default:
            return state
    }
}