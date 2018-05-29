import React from "react"
import {connect} from "react-redux"
import ArtworkItem from "./ArtworkItem"

class Favorites extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      artworks: []
    }
    this.getArworks(this.props.session.token_id)
  }

  getArworks(token) {
    const config = {
      method: 'GET',
      headers: { Authorization: 'Bearer ' + token }
    }

    fetch(`http://pitipoulpe.freeboxos.fr/api/likes/token`, config)
      .then((response) => {
        return response.json()
          .then((res) => {
            const ids = res.results

            ids.forEach( (art) => {
              this.getArwork(art.artwork_id)
            })
          })
      }).catch((err) => console.log(err))


  }

  getArwork(id) {
    fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/${id}/`)
      .then( (response) => {
        return response.json()
          .then(res => {
            const artwork = res.results[0]
            const old = this.state.artworks
            old.push(artwork)
            this.setState({
              artworks: old
            })
          })
        }
      ).catch( (err) => console.log(err))
  }

  render() {
    console.log('=>'  ,this.state.artworks)
    return(
      <div>
        <div className="logo" >
          <img src="../../../img/logo.svg" alt="logo ecv" />
        </div>
        <div className="content">
          {this.state.isLoading &&
          <span className={"loader"}></span>
          }
          {!this.state.isLoading && this.state.errorMessage &&
          <span>{this.state.errorMessage}</span>
          }
          <div>
            <p>Retrouver toutes les oeuvres que vous avez aimé !</p>
          </div>
          {!this.state.isLoading && this.state.artworks && this.state.artworks.length > 0 &&
          <ul className="artworks-grid">
            {this.state.artworks.map((data, index) => (
              <ArtworkItem key={index} id={index} artwork={data}/>
            ))}
          </ul>
          }
          {!this.state.isLoading && this.state.artworks && this.state.artworks.length === 0 &&
          <ul className="artworks-grid">
            <span>Vous n'avez aimé aucune oeuvre pour le moment</span>
          </ul>
          }
        </div>
      </div>
    )
  }
}

const mapStateToProps = (GeneralStoreToMap) => {
  return  {
    session: GeneralStoreToMap.session
  }
}

export default connect(mapStateToProps)(Favorites)