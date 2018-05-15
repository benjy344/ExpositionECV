import { getPlaceData} from '../services/place'

// ACTIONS
export const FETCH_DATA     = 'FETCH_DATA'
export const UPDATE_DATA    = 'UPDATE_DATA'
export const RECEIVE_DATA   = 'RECEIVE_DATA'

export function fetchProducts( dispatch ) {
    dispatch({type: FETCH_DATA})

    getPlaceData()
        .then(response => response.json())
        .then(data => {
            dispatch({
                type: RECEIVE_DATA,
                data: data
            })
        })
}

export function updateProducts( data ) {
    return function (dispatch) {
        dispatch({
            type: UPDATE_DATA,
            data: data
        })
    }
}
