import React from 'react'

import '../scss/main'
import ArtworkItem from "./ArtworkItem";

class Infos extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      errorMessage: null,
      content: null,
      artworks: []
    }
    this.getContent(this.props.match.params.place)
  }

  getContent(id) {
    fetch(`http://pitipoulpe.freeboxos.fr/api/places/${id}/pages/info` )
      .then( (response) => {
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

  componentWillReceiveProps(nextProps) {
    this.getPlaceContent(nextProps.match.params.place)
  }

  createMarkup(content) {
    return {__html: content }
  }

  render() {
    return(
      <div className={"infos"}>
        <div className="logo" >
          <img src="../../../img/logo.svg" alt="logo ecv" />
        </div>
        <h1 className={'sectionTitle'}>Informations Pratiques</h1>
        {this.state.errorMessage &&
        <span>{this.state.errorMessage}</span>
        }
        {this.state.content &&
        <div className={'content-info'} dangerouslySetInnerHTML={this.createMarkup(this.state.content)} ></div>
        }
      </div>
    )
  }
}

export default Infos