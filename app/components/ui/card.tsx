export function Card({ children, className }: { children: React.ReactNode; className?: string }) {
    return (
      <div className={`bg-white shadow-lg rounded-lg p-6 ${className}`}>
        {children}
      </div>
    );
  }
  
  export function CardContent({ children }: { children: React.ReactNode }) {
    return <div className="text-gray-700">{children}</div>;
  }
  