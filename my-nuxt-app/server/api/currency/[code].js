export default defineEventHandler(async (event) => {
    const {code} = event.context.params;
    const {currencyKey} = useRuntimeConfig();
    const uri = `https://api.currencyapi.com/v3/latest?currencies=${code}&apiKey=${currencyKey}`;
    //const uri = `https://api.currencyapi.com/v3/latest?currencies=${code}`;
    console.log('uri', uri)
    //return {
    //    uri: uri
    //}
    const {data} = await $fetch(uri, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'apikey': currencyKey

        }
    });
    return data
})
