
// ACTIONS
export const GET_UNIQUE_ID = 'GET_UNIQUE_ID'

export function getUniqueId( token ) {
  return function (dispatch) {
    dispatch({
      type: GET_UNIQUE_ID,
      token_id: token
    })
  }
}
