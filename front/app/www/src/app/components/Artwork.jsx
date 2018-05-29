import React     from 'react'
import { Link }  from 'react-router-dom'
import jwt from 'jsonwebtoken'


class ArtworkItem extends React.Component {
  constructor(props) {
    super(props)
    console.log(this.props.match.params.id)
    this.state = {
      liked: false,
      errorMessage: null,
      artwork: {},
      author: {}
    }
    fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/${this.props.match.params.id}/` )
      .then( (response) => {
        if(!response.ok){
          this.setState({
            errorMessage:response.statusText
          })
        } else {
          response.json()
            .then(resp => {
              const content = resp.results[0]
              this.setState({
                artwork: content
              }, () => {
                this.getAuthor(content.author_id)
              })
            })
        }
      })
      .catch(err => console.log("Error: ", err))
  }

  getAuthor(id) {
    fetch(`http://pitipoulpe.freeboxos.fr/api/authors/${id}/`)
      .then(response => {
        if(!response.ok){
          this.setState({
            errorMessage:response.statusText
          })
        } else {
          response.json()
            .then(resp => {
              const author = resp.results[0]
              this.setState({
                author
              })
            })
        }
      })
  }



  render() {
    return (
      <article className="unique-artwork-details">
        <figure className="artwork-image">
          <section className="artwork-image-container">
            <img src={'../../../img/img.jpeg'} alt="Image de Benoit DELDIQUE - E-Pistolaire" />
          </section>
          <figcaption className="artwork-details-caption">
            <p className="artwork-map-number">29</p>
            <section className="artwork-title-container">
              <p className="artwork-title">{this.state.artwork.name}</p>
              <p className="artwork-artist">{this.state.author.name} {this.state.author.firstname}</p>
            </section>
            <div className="artwork-line"><hr /></div>
            <div className="artwork-favorite share-icon" >
              <i className="fas fa-heart favorite-like" />
            </div>
            <div className="artwork-details-share">
              <i className="fas fa-share-alt share-icon" />
              <div className="share-icons">
                <a href="#" >
                  <i className="fab fa-facebook-square share-icon" />
                </a>
                <a href="https://twitter.com/intent/tweet?text=E-Pistolaire%20par%20Benoit DELDIQUE%20@ECV_Digital%20https://expo.ecvdigital.fr/oeuvre/s/benoit-deldique-e-pistolaire">
                  <i className="fab fa-twitter-square share-icon" />
                </a>
                <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://expo.ecvdigital.fr/oeuvre/s/benoit-deldique-e-pistolaire&title=E-Pistolaire%20par%20Benoit DELDIQUE&summary=&source=">
                  <i className="fab fa-linkedin share-icon" />
                </a>
              </div>
            </div>
          </figcaption>
        </figure>
        <section className="artwork-description-container">
          <div className="artwork-description-quote icon-quote">
          </div>
          <p className="artwork-description">
            Plus digitaux que jamais, nos échanges se font par
            le biais d’outils aussi différents que complémentaires.
            Quelle est donc cette nouvelle continuité naissante et
            comment la retranscrit-on ?
          </p>
        </section>
      </article>

    )
  }
}

export default ArtworkItem