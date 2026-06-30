interface StatusChipProps {
  label: string
}

export function StatusChip({ label }: StatusChipProps) {
  return <span className="status-chip">{label}</span>
}
