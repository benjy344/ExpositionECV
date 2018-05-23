import { getPlaceData} from '../services/place'

// ACTIONS
export const FETCH_PLACES     = 'FETCH_PLACES'
export const UPDATE_PLACES    = 'UPDATE_PLACES'
export const RECEIVE_PLACES   = 'RECEIVE_PLACES'

export function fetchPlaces( dispatch ) {
    dispatch({type: FETCH_PLACES})

    getPlaceData()
        .then(response => response.json())
        .then(data => {
            dispatch({
                type: RECEIVE_PLACES,
                data: data
            })
        })
}

export function updatePlaces( data ) {
    return function (dispatch) {
        dispatch({
            type: UPDATE_PLACES,
            data: data
        })
    }
}
