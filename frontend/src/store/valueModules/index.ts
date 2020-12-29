

interface ValueState {
    value: number;
}

const state: ValueState = {
    value: 0
}

const actions = {
    async addPlus({commit}: any) {
        const response = await commit("ADD_VALUES");
        return response;
    },
    async addOdd({commit}: any) {
        const response = await commit("ODD_VALUES");
        return response;
    },
}

const mutations = {
    ADD_VALUES: (data: ValueState, values: any) => {
        if(data.value < 30) {
            data.value ++;
        }
        return;
    },
    ODD_VALUES: (data: ValueState, values: any) => {
        if(data.value !== 0) {
            data.value --
        }
        return;
    }
}

const getters = {
    value: (data: ValueState) => data.value,
};



export default {
    state,
    actions,
    mutations,
    getters,
};