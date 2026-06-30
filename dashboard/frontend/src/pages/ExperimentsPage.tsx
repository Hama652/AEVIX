import { PlaceholderChart } from '../components/ui/PlaceholderChart'
import { SectionCard } from '../components/ui/SectionCard'

export function ExperimentsPage() {
  return (
    <div className="page-stack">
      <SectionCard title="Experiments" subtitle="Experiment tracking will connect to the backend in a future phase.">
        <div className="empty-state">No active experiments</div>
      </SectionCard>
      <SectionCard title="Comparison" subtitle="Comparison views will appear once experiment records exist.">
        <PlaceholderChart title="Comparison Placeholder" caption="No data is displayed until experiment tracking is integrated." />
      </SectionCard>
    </div>
  )
}
