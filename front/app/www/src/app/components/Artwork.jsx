import React     from 'react'
import { Link }  from 'react-router-dom'
import jwt from 'jsonwebtoken'


class ArtworkItem extends React.Component {
  constructor(props) {
    super(props)
    console.log(this.props.match.params.id)
    this.state = {
      liked: false
    }
    fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/${this.props.match.params.id}/` )
      .then( (response) => {
        console.log(response)
        if(!response.ok){
          this.setState({
            errorMessage:response.statusText
          })
        } else {
          response.json()
            .then(resp => {
              console.log(resp)
              const content = resp.results[0].text
              this.setState({
                content
              })
            })
        }
      })
      .catch(err => console.log("Error: ", err))
  }

  like(id) {
    if(localStorage.getItem('id_token')) {

    } else {
      const cert = this.guid()
      let token = jwt.sign({ dateTime: new Date().getMilliseconds() }, cert)
      localStorage.setItem('id_token', token)
    }
  }

  render() {
    return (
      <div>
        <div>Hello Artwork</div>
        <button onClick={this.like.bind(this, this.props.match.params.id)}>Link</button>
      </div>

    )
  }
}

export default ArtworkItem