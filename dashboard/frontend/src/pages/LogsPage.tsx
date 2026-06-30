import { SectionCard } from '../components/ui/SectionCard'

export function LogsPage() {
  return (
    <SectionCard title="Logs" subtitle="Live log streaming will be attached later.">
      <div className="empty-state">No live logs connected</div>
    </SectionCard>
  )
}
