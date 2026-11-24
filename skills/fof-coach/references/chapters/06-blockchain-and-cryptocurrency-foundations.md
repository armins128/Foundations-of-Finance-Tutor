# 6. Blockchain and cryptocurrency foundations

## 6.1 Cryptocurrency and blockchain

A **cryptocurrency** is a digitally represented asset that can be transferred through an electronic network using cryptographic methods. Bitcoin is a cryptocurrency. A cryptocurrency can be bought and sold online, but the ability to trade it does not guarantee its value, liquidity, legality, safety, or future price.

A **blockchain** is a digital ledger in which information is grouped into blocks and linked in sequence. Cryptographic hashes help make later alteration detectable. Copies of the ledger can be maintained across a network rather than by one central clearing house.

The classical intermediary-based model relies on a trusted central party to maintain records and validate transfers. A decentralized blockchain-based model instead uses a protocol and a consensus mechanism so that network participants can agree on the valid history of transactions.

Important distinctions:

- A blockchain is a record-keeping technology; it is not identical to Bitcoin.
- Bitcoin uses a blockchain, but blockchains can support many other assets and applications.
- A cryptocurrency token is not automatically an ownership share in a company. Ownership rights depend on the legal and contractual design of the asset.
- A public ledger can make transaction records visible while users are represented by addresses rather than ordinary names. This is better described as pseudonymity than guaranteed anonymity.

## 6.2 Transactions, blocks, hashes, and the ledger

A simplified transaction process is:

1. A user authorizes a transaction using cryptographic credentials.
2. The transaction is broadcast to the network.
3. Network participants validate it under the protocol's rules.
4. Valid transactions are collected into a block.
5. A consensus mechanism determines how a new block is accepted.
6. The accepted block becomes part of the ledger replicated across the network.

A **hash function** maps input data to a fixed-length output. A small input change produces a different hash. Blocks refer cryptographically to prior data, so changing an old record would disrupt later links and be detectable. This supports tamper evidence, though the security of a real system also depends on network incentives, implementation, governance, and control of consensus resources.

A blockchain helps address the **double-spending problem**: without a trusted intermediary, the network still needs a consistent method for deciding whether the same digital unit has already been transferred elsewhere.

## 6.3 Consensus mechanisms

A consensus mechanism aims to:

- establish agreement about the state and transaction history of the network;
- prevent conflicting transaction histories and double spending;
- give participants incentives to follow the protocol.

### Proof of work

In **proof of work (PoW)**, miners compete using computing power to solve a computational puzzle. The successful miner can propose a block and receive protocol-defined rewards and fees. Rewriting history would require substantial computational resources. The mechanism can be energy intensive.

Bitcoin uses proof of work. New bitcoins are issued through block rewards according to protocol rules. The reward decreases over time, and the protocol limits the maximum bitcoin supply to approximately 21 million coins. Limited supply does not guarantee a stable or rising market price; demand and market conditions still matter.

### Proof of stake

In **proof of stake (PoS)**, validators commit or lock tokens as stake. The protocol selects validators according to its rules, and dishonest behavior can be penalized. PoS avoids the same type of computational competition used by PoW and can require substantially less energy, but it has its own concentration, governance, and implementation risks.

### Proof of history

**Proof of history (PoH)** is a cryptographic ordering mechanism associated with Solana. It provides a verifiable sequence of events and works together with the network's broader consensus design. It should not be confused with proof of work or treated as a complete substitute for all consensus functions by itself.

## 6.4 Cryptoassets, NFTs, and economic rights

Different digital tokens can represent different claims or functions:

- a native cryptocurrency may be used for network transfers, fees, or incentives;
- a utility token may provide access to a service;
- a governance token may provide specified voting rights;
- a stablecoin seeks to track a reference asset but is exposed to design, reserve, counterparty, and market risks;
- a non-fungible token (NFT) is a unique token identifier that can be linked to a digital or physical item.

Owning a token does not automatically confer copyright, company ownership, profit participation, redemption rights, or control over an underlying asset. Those rights depend on the applicable contract and legal framework.

## 6.5 Risks and misconceptions

Cryptoassets can involve:

- extreme price volatility;
- liquidity risk;
- operational and cybersecurity risk;
- loss of private credentials;
- smart-contract or protocol failures;
- counterparty and custody risk;
- regulatory and legal uncertainty;
- manipulation, fraud, and misleading marketing;
- environmental costs, particularly for energy-intensive consensus mechanisms.

Common misconceptions include:

- **“Digital means risk-free.”** Digital assets can lose most or all of their value.
- **“A fixed supply guarantees price appreciation.”** Price depends on both supply and demand.
- **“A branded token is a share in the associated person or business.”** A token conveys only the rights actually specified.
- **“Blockchain records are secret.”** Public blockchains can expose transaction histories even when addresses are pseudonymous.
- **“Blockchain removes the need for trust.”** Trust is redistributed toward software, protocol rules, validators, custodians, governance, and users' security practices.

---
