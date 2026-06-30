interface PlaceholderChartProps {
  title: string
  caption: string
}

export function PlaceholderChart({ title, caption }: PlaceholderChartProps) {
  return (
    <div className="chart-placeholder" aria-label={title}>
      <div className="chart-placeholder__title">{title}</div>
      <div className="chart-placeholder__canvas" aria-hidden="true">
        <div className="chart-placeholder__grid" />
        <div className="chart-placeholder__pulse" />
      </div>
      <p className="chart-placeholder__caption">{caption}</p>
    </div>
  )
}
