import {
  GET_UNIQUE_ID
} from '../actions/session'

// Defined a default state
export const initialState = {
  token_id: ''
}

export function session(state = initialState, action) {
  switch (action.type) {
    case GET_UNIQUE_ID:
      return Object.assign({}, state, {
        token_id: action.token_id
      })

    default:
      return state
  }
}