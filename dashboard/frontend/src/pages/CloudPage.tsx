import { SectionCard } from '../components/ui/SectionCard'

export function CloudPage() {
  return (
    <SectionCard title="Cloud" subtitle="Cloud GPU management is reserved for future integration.">
      <div className="empty-state">No active cloud connection</div>
    </SectionCard>
  )
}
