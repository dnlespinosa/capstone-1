async function getData() {
    const res = await axios.get('http://csgobackpack.net/api/GetItemsList/v2/')
    console.log(res.data)
}