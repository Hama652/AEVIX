import { PlaceholderChart } from '../components/ui/PlaceholderChart'
import { SectionCard } from '../components/ui/SectionCard'

export function DashboardPage() {
  return (
    <div className="page-grid">
      <SectionCard title="Training Status" subtitle="Live orchestration is not enabled in this phase.">
        <div className="empty-state">No active training</div>
      </SectionCard>

      <SectionCard title="GPU Usage" subtitle="Reserved for future accelerator telemetry.">
        <PlaceholderChart title="GPU Usage Placeholder" caption="Instrumentation will appear here once live GPU metrics are integrated." />
      </SectionCard>

      <SectionCard title="Recent Experiments" subtitle="Experiment tracking will connect in a later phase.">
        <div className="empty-state">No active experiments</div>
      </SectionCard>

      <SectionCard title="Model Information" subtitle="Model lifecycle integration is intentionally absent.">
        <div className="empty-state">No active models</div>
      </SectionCard>

      <SectionCard title="Cloud Connection" subtitle="Cloud orchestration surfaces are reserved for future use.">
        <div className="empty-state">No active cloud connection</div>
      </SectionCard>
    </div>
  )
}
