export const formatUGX = (amount: number) =>
  `UGX ${amount.toLocaleString('en-UG', { maximumFractionDigits: 2 })}`

export const formatPercent = (value: number) =>
  `${value >= 0 ? '+' : ''}${value.toFixed(2)}%`

export const formatDate = (date: string) =>
  new Date(date).toLocaleDateString('en-UG', { day: 'numeric', month: 'short', year: 'numeric' })
