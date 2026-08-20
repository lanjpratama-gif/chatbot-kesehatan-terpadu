# Diagram Alur Chatbot Kesehatan Terpadu

## Alur Sistem

```text
┌─────────────────────┐
│     User Input      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Cek Urgensi       │
│   (Guardrail)       │
└──────────┬──────────┘
           │
           ▼
      ┌───────────┐
      │ Darurat?  │
      └─────┬─────┘
         Ya │  │ Tidak
            │  │
            ▼  ▼
┌──────────────────┐   ┌─────────────────────┐
│   Eskalasi Medis │   │ Cek Permintaan      │
│                  │   │ Obat / Dosis        │
└──────────────────┘   └──────────┬──────────┘
                                  │
                                  ▼
                         ┌────────────────┐
                         │ Obat / dosis?  │
                         └───────┬────────┘
                            Ya   │   │ Tidak
                                 │   │
                                 ▼   ▼
                         ┌───────────┐ ┌─────────────────┐
                         │ Tolak     │ │ Cek Scope       │
                         │ Permintaan│ │ Kesehatan       │
                         └───────────┘ └────────┬────────┘
                                               │
                                               ▼
                                      ┌─────────────────┐
                                      │ Dalam Scope?    │
                                      └────────┬────────┘
                                          Ya   │   │ Tidak
                                               │   │
                                               ▼   ▼
                                         ┌──────────┐
                                         │  OpenAI  │
                                         │   API    │
                                         └────┬─────┘
                                              │
                                              ▼
                                         ┌──────────┐
                                         │ Respons  │
                                         │ Chatbot  │
                                         └──────────┘