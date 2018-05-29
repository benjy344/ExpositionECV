import React             from 'react'
import {history, Store}  from "../generalStore/Store"
import {Provider}        from "react-redux"
import {ConnectedRouter} from "react-router-redux"
import { Route, Redirect }         from 'react-router'

import Nav               from "./Nav"
import Favorites         from "./Favorites"
import Artwork           from "./Artwork"
import Home              from "./Home"
import Infos             from "./Infos"

import { getUniqueId } from '../actions/session'
import jwt from "jsonwebtoken"




class App extends React.Component {

  constructor(props) {
    super(props)

    if(localStorage.getItem('id_token')) {
      Store.dispatch(getUniqueId(localStorage.getItem('id_token')))
    } else {
      const cert = this.guid()
      let token = jwt.sign({ dateTime: new Date().getMilliseconds() }, cert)
      localStorage.setItem('id_token', token)
      Store.dispatch(getUniqueId(token))
    }
  }

  guid() {
    return this.s4() + this.s4() + '-' + this.s4() + '-' + this.s4() + '-' +
      this.s4() + '-' + this.s4() + this.s4() + this.s4()
  }

  s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }


  render() {
    return(
      <Provider store={Store}>
        <ConnectedRouter history={history}>
          <div>
            <Nav />
            <Route exact path="/" render={() => (
                <Redirect to="/1/home"/>
            )}/>
            <Route exact path="/:place/home" component={Home}/>
            <Route path="/:place/infos" component={Infos}/>
            <Route path="/favorites" component={Favorites}/>
            <Route path="/artwork/:id" component={Artwork}/>
          </div>
        </ConnectedRouter>
      </Provider>
    )
  }
}

export default App