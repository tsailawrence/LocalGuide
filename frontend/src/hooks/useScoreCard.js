import { createContext, useContext, useState } from 'react'

const ADD_MESSAGE_COLOR = '#3d84b8'
const REGULAR_MESSAGE_COLOR = '#2b2e4a'
const ERROR_MESSAGE_COLOR = '#fb3640'

const ScoreCardContext = createContext({
    messages: [],
    clearMessage: {},
    addCardMessage: () => {},
    addRegularMessage: () => {},
    addErrorMessage: () => {},
})

const makeMessage = (message, color) => {
    return { message, color }
}

const ScoreCardProvider = (props) => {
    const [messages, setMessages] = useState([])
    const [clearMessage, setClearMessage] = useState({})

    const addClearMessage = (message) => {
        setClearMessage(makeMessage(message, ADD_MESSAGE_COLOR))
    }

    const addCardMessage = (message) => {
        setClearMessage({})
        setMessages([...messages, makeMessage(message, ADD_MESSAGE_COLOR)])
    }

    const addRegularMessage = (...ms) => {
        setClearMessage({})
        setMessages([
            ...messages,
            ...ms.map((m) => makeMessage(m, REGULAR_MESSAGE_COLOR)),
        ])
    }

    const addErrorMessage = (message) => {
        setClearMessage({})
        setMessages([...messages, makeMessage(message, ERROR_MESSAGE_COLOR)])
    }

    const deleteMessage = () => {
        setMessages([])
    }

    return (
        <ScoreCardContext.Provider
            value={{
                messages,
                clearMessage,
                addClearMessage,
                addCardMessage,
                addRegularMessage,
                addErrorMessage,
                deleteMessage,
            }}
            {...props}
        />
    )
}

function useScoreCard() {
    return useContext(ScoreCardContext)
}

export { ScoreCardProvider, useScoreCard }
