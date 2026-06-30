import { PlaceholderChart } from '../components/ui/PlaceholderChart'
import { SectionCard } from '../components/ui/SectionCard'

export function TrainingPage() {
  return (
    <div className="page-stack">
      <SectionCard title="Training Control" subtitle="The orchestration layer is reserved for a future implementation.">
        <div className="empty-state">No active training</div>
      </SectionCard>
      <SectionCard title="Training Metrics" subtitle="This card will host live metrics once training jobs exist.">
        <PlaceholderChart title="Training Metrics Placeholder" caption="No data is displayed until training is wired in." />
      </SectionCard>
    </div>
  )
}
