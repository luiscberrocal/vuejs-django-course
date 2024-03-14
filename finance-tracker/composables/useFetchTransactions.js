export const useFetchTransactions = () => {
    const transactions = ref([]);
    const pending = ref(false);
    const supabase = useSupabaseClient();

    const income = computed(() => transactions.value.filter(transaction => transaction.type === 'Income'));
    const expense = computed(() => transactions.value.filter(transaction => transaction.type === 'Expense'));

    const incomeCount = computed(() => income.value.length);
    const expenseCount = computed(() => expense.value.length);

    const incomeTotal = computed(() => income.value.reduce((sum, transaction) => sum + transaction.amount, 0));
    const expenseTotal = computed(() => expense.value.reduce((sum, transaction) => sum + transaction.amount, 0));

    const fetchTransactions = async () => {
        pending.value = true;
        try {
            const {data} = await useAsyncData('transactions',
                async () => {
                    const {data, error} = await supabase.from('transactions')
                        .select('*')
                        .order('created_at', {ascending: false})
                    console.log('>>> DATA', data);
                    return data;
                    if (error) {
                        //return []
                        throw error;
                    }
                    return data
                });
            return data.value;
        } catch (error) {
            console.error('>>> ERROR', error);
        } finally {
            pending.value = false;
        }
    }

    const refresh = async () => transactions.value = await fetchTransactions();

    const transactionsGroupedByDate = computed(() => {
        let grouped = {}
        for (const transaction of transactions.value) {
            const date = new Date(transaction.created_at).toISOString().split('T')[0]
            if (!grouped[date]) {
                grouped[date] = []
            }
            grouped[date].push(transaction)
        }
        return grouped
    })

    return {
        transactions: {
            all: transactions,
            grouped: {
                byDate: transactionsGroupedByDate
            },
            income,
            expense,
            incomeCount,
            expenseCount,
            incomeTotal,
            expenseTotal,
        },
        refresh,
        pending,
    }

}
