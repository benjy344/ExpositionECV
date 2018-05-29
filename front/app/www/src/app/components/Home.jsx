import React from 'react'

import '../scss/main'
import ArtworkItem from "./ArtworkItem";

class Home extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      errorMessage: null,
      content: null,
      isLoading: true,
      artworks: []
    }

    this.getPlaceContent(this.props.match.params.place)
    this.getArtworks()
  }

  getPlaceContent(id) {
    fetch(`http://pitipoulpe.freeboxos.fr/api/places/${id}/pages/home` )
      .then( (response) => {
        console.log(response)
        if(!response.ok){
          this.setState({
            isLoading: false,
            errorMessage:response.statusText
          })
        } else {
          response.json()
            .then(resp => {
              console.log(resp)
              const content = resp.results[0].text
              this.setState({
                isLoading: false,
                content
              })
            })
        }
      })
      .catch(err => console.log("Error: ", err))
  }

  getArtworks() {
    fetch(`http://pitipoulpe.freeboxos.fr/api/artworks` )
      .then( (response) => {
        if(!response.ok){
          this.setState({
            isLoading: false,
            errorMessage:response.statusText
          })
        } else {
          response.json()
            .then(resp => {
              console.log(resp)
              const artworks = resp.results
              this.setState({
                isLoading: false,
                artworks
              })
            })
        }
      })
      .catch(err => console.log("Error: ", err))
  }

  componentWillReceiveProps(nextProps) {
    this.setState({
      isLoading: true
    })
    this.getPlaceContent(nextProps.match.params.place)
  }

  createMarkup(content) {
    return {__html: content }
  }

  render() {
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
          {!this.state.isLoading && this.state.content &&
          <div dangerouslySetInnerHTML={this.createMarkup(this.state.content)} ></div>
          }
          {!this.state.isLoading && this.state.artworks && this.state.artworks.length &&
          <ul className="artworks-grid">
            {this.state.artworks.map((data, index) => (
              <ArtworkItem key={index} id={index} artwork={data}/>
            ))}
          </ul>
          }
        </div>
      </div>
    )
  }
}

export default Home