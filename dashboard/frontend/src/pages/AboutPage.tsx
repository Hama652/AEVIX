import { SectionCard } from '../components/ui/SectionCard'

export function AboutPage() {
  return (
    <SectionCard title="About" subtitle="AEVIX dashboard foundation for long-term operational growth.">
      <div className="about-copy">
        <p>
          This interface is the starting point for the AEVIX operational dashboard. It is designed
          to support future training jobs, experiment tracking, checkpoint management, cloud GPU
          controls, and live logs without redesigning the UI architecture.
        </p>
        <p>No AI model, training loop, or dataset pipeline is implemented in this phase.</p>
      </div>
    </SectionCard>
  )
}
