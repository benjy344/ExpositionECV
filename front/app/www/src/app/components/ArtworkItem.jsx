import React       from 'react'
import { Link }    from 'react-router-dom'
import { connect } from 'react-redux'



class ArtworkItem extends React.Component {
  constructor(props) {
    super(props)
    const currentLikes = JSON.parse(localStorage.getItem(`like-${this.props.session.token_id}`)) || []
    const isLiked = currentLikes.filter( (item)=> {
      return item === this.props.artwork.id
    })
    this.state = {
      liked: isLiked.length > 0
    }
  }

  like(id) {
    const config = {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + this.props.session.token_id }
    }
    if(this.state.liked) {
      //unlike
      fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/${id}/removelike`, config)
        .then((response) => {
          response.json()
            .then((res) => {
              if (res.results && res.results === 'OK') {
                this.setState({
                  liked:false
                }, () => {
                  const currentLikes = JSON.parse(localStorage.getItem(`like-${this.props.session.token_id}`)) || []
                  const newLikes = currentLikes.filter( (item)=> {
                    return item !== id
                  })
                  localStorage.setItem(`like-${this.props.session.token_id}`, JSON.stringify(newLikes))
                })
              }
            })
        })
        .catch( (err) => console.error(err))
    } else {
      fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/${id}/addlike`, config)
        .then((response) => {
          response.json()
            .then((res) => {
              if (res.results && res.results === 'OK') {
                this.setState({
                  liked:true
                }, () => {
                  const currentLikes = JSON.parse(localStorage.getItem(`like-${this.props.session.token_id}`)) || []
                  currentLikes.push(id)
                  localStorage.setItem(`like-${this.props.session.token_id}`, JSON.stringify(currentLikes))
                })
              }
            })
        })
        .catch( (err) => console.error(err))
    }
  }

  render() {
    return (
      <li className={"artwork "}>
        <div className="artwork-image">
          <Link to={`/artwork/${this.props.id}`}>
            <img src={'../../../img/'+this.props.artwork.img+'.jpeg'} alt={this.props.artwork.name} />
          </Link>
        </div>
        <div className="artwork-details">
          <h3><a href="#0">{this.props.artwork.name}</a></h3>
        </div>
        <button className={"like-item "+(this.state.liked? 'icon-fullHeart' : 'icon-heart') } onClick={this.like.bind(this, this.props.artwork.id)}></button>
      </li>
    )
  }
}

const mapStateToProps = (GeneralStoreToMap) => {
  return  {
    session: GeneralStoreToMap.session
  }
}

export default connect(mapStateToProps)(ArtworkItem)