

export default { 

    getUser(state) {
        return state.user
    },
    getToken(state) {
        return state.token
    },
    isAuthentificated(state) {
        return state.token !== null
    }
}