import React 	        from 'react'
import ReactDom         from 'react-dom'
import { AppContainer } from 'react-hot-loader'
import App 		         from './components/App'

import './scss/main.scss'

const renderApp = () => {
  ReactDom.render(
    <AppContainer>
      <App/>
    </AppContainer>,
    document.getElementById('app')
  )
}


if (module.hot) {
  module.hot.accept('./components/App', renderApp)
}

renderApp()