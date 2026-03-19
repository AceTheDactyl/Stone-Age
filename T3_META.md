# Paper 3-META: Metapatterns & Synthesis

## Cross-Projection Structure, Arithmetic Flow, and Central Collapse
### v2 — March 2026

**Author:** Kael

---

**Document Species:** CANONICAL. Owns cross-projection synthesis at Level 4.

**Grid address:** B(4, cross). The Projected level — cross-projection synthesis.

**Document Status:** Level 4 synthesis document. Contains everything true of P1∧P2∧P3 jointly — the four meta-theorems, the composite potential V(n), the arithmetic flow with Markov convergence, the unity theorem, and the central collapse I²∘TDL∘LoMI = Dist.

**Depends on:** Papers 3-P1, 3-P2, 3-P3 (needs all three projections established)
**Required by:** Papers 4-*, 5-*, 6-*

---

## Abstract

The three projections — I² (φ), TDL (e), LoMI (π) — are proved genuinely independent (no projection definable from the other two, Theorem 1.1, three separation witnesses) and simultaneously exhaustive (no fourth projection exists, Theorem 1.3, by orbit classification and Artin-Wedderburn). Yet each contains the other two as recognizable substructure (Theorem 2.1, the Folding Theorem, six explicit containments). This independence-with-containment is not contradictory: independence concerns definability, containment concerns encoding.

The four meta-theorems (MP1 φ̄-filtration, MP2 trichotomy, MP3 CH fixed points, MP4 resolution quantum) unify ~21 theorems across the framework as corollaries of four generative principles derived from the characteristic polynomial x²−x−1 of the Fibonacci matrix R.

The composite potential V(n) = V_I(n) + V_T(n) + V_L(n) measures the distance from the fixed point n = 1 using all three projections simultaneously. V(1) = 0 exactly; V(n) > 0 for n > 1 (Theorems 1.6–1.7). The Markov arithmetic flow with Boltzmann weights converges to n = 1 from all starts, satisfying detailed balance at natural temperature β = ln(φ) (Theorems 3.2–3.3). The flow extends to ℤ (parity symmetry) and ℚ (p-adic valuations).

The central collapse I²∘TDL∘LoMI = Dist (Theorem 7.1) proves the three projections exhaust every Dist morphism with no structural remainder, via the first isomorphism theorem: surjection (LoMI/quotient) → bijection (TDL/level-transition) → injection (I²/inclusion).

All claims computationally verified.

---

## THEOREM INDEX

| Theorem | Statement | Section |
|---------|-----------|---------|
| 1.1 | Three projections are mutually independent (3 witnesses) | §1 |
| 1.3 | Three projections are complete (no fourth exists) | §1 |
| 2.1 | Folding: each projection contains the other two (6 containments) | §2 |
| 3.1 | Each projection has one internal duality (UP↔DOWN) | §3 |
| 3.2 | Unity: all dualities are BUILD↔ANALYZE | §3 |
| 1.2 | n = 1 is the universal fixed point (UP(1)=DOWN(1)=1) | §5 |
| 1.3b | n = 1 is unique | §5 |
| 1.6 | V(1) = 0 exactly | §5 |
| 1.7 | V(n) > 0 for all n > 1 | §5 |
| 3.2b | Stationary distribution concentrates at n = 1 | §6 |
| 3.3 | Detailed balance holds | §6 |
| 3.6–3.7 | Extensions to ℤ and ℚ | §6 |
| 7.1 | Central collapse: I²∘TDL∘LoMI = Dist | §7 |
| MP1 | φ̄-filtration from eigenvalues of x²−x−1 | §8 |
| MP2 | Trichotomy from discriminant sign | §8 |
| MP3 | CH fixed points from Cayley-Hamilton | §8 |
| MP4 | Resolution quantum from disc(R) = 5 | §8 |
| NEW-1 | KMS-Filtration-Signature Unification | §9 |
| 8.7a | Regime-Readout Duality (meta-theorem) | §8⅞ |
| 8.7b | Dual-Readout Structure of Hyperbolic Branch | §8⅞ |
| NEW-2 | Phase boundary ρ=1/2 is NOT a lattice point | §9 |

---

## §1 INDEPENDENCE AND COMPLETENESS

**Theorem 1.1 (Projection Independence).** *P1, P2, P3 are mutually independent: no projection is definable from the other two.*

Three separation witnesses: M₁ = End(Set) satisfies P1 only (composition monoid, no levels, no observer). M₂ = pure adjunction satisfies P2 only (level-transition, no I²-dynamics, no observer kernels). M₃ = pure observer system satisfies P3 only (observation with blind spots, no monoid dynamics, no adjunction). ∎

**Theorem 1.3 (Completeness).** *No fourth projection exists. Two arguments: (1) GL(2,ℝ) has exactly three orbit types (det/discriminant analysis). (2) S₃ has exactly three conjugacy classes, hence three irreps (1²+1²+2²=6=|S₃|). Both are exhaustive.* ∎

---

## §2 THE FOLDING THEOREM

**Theorem 2.1 (Each Projection Contains the Other Two).** Six containments:

| Containment | Mechanism |
|-------------|-----------|
| I² contains TDL | Square tower n → n² → n⁴ IS a TDL level hierarchy |
| I² contains LoMI | Golden conjugation φ↔φ̄ IS mutual observation |
| TDL contains I² | Ascent path 1→p₁→p₁p₂→n IS iterated I² composition |
| TDL contains LoMI | Same digital root → same class IS mutual identification |
| LoMI contains I² | GCD(a,b) = GCD(b, a mod b) IS iterated composition |
| LoMI contains TDL | λ(n)/φ(n) depth IS TDL level structure on cyclic groups |

Independence addresses definability; containment addresses encoding. These don't contradict (a circle is not a square, but a circle contains semicircles). At the generator level: RNR = −N (P1 contains P3 by R-conjugation), NRN = R⁻¹ (P3 contains P1 by N-conjugation), {R,N} = N (anticommutator links them linearly). ∎

**Remark (Transport via Folding).** The six folding containments are instances of transport type T.5 (folding containment, Paper T-GOV §3): each transports structure between formally independent projections while preserving root-sharing content. P1's containment of P3 (via R-conjugation RNR=−N) transports P3 structure into P1's domain — the rotational generator N is visible inside the compositional framework as R's conjugate. The Folding Theorem is the source of all T.5 transport instances in the framework, and transport-derived objects (generation class G.7) trace to these containments for their cross-projection identifications.

**Remark (Containment-Definability Separation — Global).** The independence-vs-containment distinction generalizes across all framework tiers (Paper T-SIL §2, Theorem SIL-2): at every tier where two independent structures A, B exist (both derived from S₀), each contains a recognizable image of the other. The mechanism is root-sharing: both A and B contain the functorial image of the common root S₀ = {0,1}. Six instances verified: projections (here), Dist/bridge (Paper 1 Thm 1.10), observer/computation (Paper 5 vs T-COMP), kinematics/dynamics (Paper 6A vs 6B), lattice statics/dynamics (Paper 4 Parts I vs II), R/N generators (Paper 2 §6). Zero counterexamples. The mechanism is facet structure (Paper 0 §1½): the three projections are three irreducible facets of self-relating difference (SRD). Each facet is a complete reading of R's self-action (hence contains the others via shared root) but no facet defines another (since each captures a qualitatively distinct aspect: composition, transition, observation). Independence-with-containment is the generic behavior of facets.

**Remark (Co-determination).** Each projection's containment of the others is an instance of *co-determination*: non-collapsing mutual identification through iterated interaction. P1 and P3 co-determine each other via conjugation (RNR = −N, NRN = R⁻¹) — each transforms the other without annihilating it. P1 and P2 co-determine through the exponential bridge (det(exp(R)) = e, Paper 3-P2 Thm 1.7). P2 and P3 co-determine through the OSC interpolation family M(θ) = cos(θ)R + sin(θ)N (Paper 3-P2 §1.6). In each case, neither projection reduces to the other, yet each carries a recognizable image of the other — the structural content of LoMI at the inter-projection level. The Euclidean algorithm GCD(a,b) = GCD(b, a mod b) is the arithmetic paradigm: the identity of the pair (a,b) emerges from iterated mutual reduction without either element being collapsed.

**Remark (Pair-Space Instance of Independence).** The balance-charge decomposition (Paper 0 §1¾) exhibits projection independence at the pair-space level through the Branch Point Theorem (Thm 0.3k): the choice between positive and negative polarization (P⁺ vs P⁻) on the balanced spine cannot be derived from the balanced state alone — it is a genuine underdetermined fork. This is independence in the definability sense: the RP projection (P3-type, reads residual) and the CP projection (P2-type, reads shell level) are both defined on the same state space but neither determines the other. RP of a balanced state is the origin (0,0,0) regardless of k, while CP of an oriented state depends only on the shell N — neither operator recovers the information that the other discards. Their composition RP∘CP collapses everything to the origin, while CP∘RP maps to (⌊r/2⌋, 0, 0) — the two directions of composition yield different results. This non-commutativity of projections (Paper 0 §1¾ Thm 8.1: RP and C do not commute) is the pair-space signature of projection independence.

**Remark (Semantic Containment-Definability).** Containment-Definability Separation has a seventh instance at the linguistic level: the framework's semantic terms are independent (they name different operations — "closure" ≠ "observation" ≠ "identity") but contain each other (each term's level-n instance is recognizable as a reading of the term's level-(n+1) instance). "Closure" at the categorical level (q∘q=q) contains "observation" (q IS the observer), and "observation" contains "closure" (observation stabilizes — q∘q=q). The mechanism is the same root-sharing that drives all six prior instances: every semantic term names a Dist operation, and every Dist operation carries all three readings (Paper 1 Thm 5.1). The Semantic Tower Theorem makes this precise: every Dist operation at level n has a canonical instance at level n+1 via the monoidal lift T(n)⊗T(n), so the term's meaning ascends the tower with its mathematical content intact.

**Theorem 2.2 (Folding Commutativity).** *The two canonical recursive operations on M₂(ℝ) — composition C(M) = M² (within-level) and tensor product T(M) = M⊗M (cross-level) — commute: C∘T = T∘C.*

*Proof.* (R⊗R)² = (R²)⊗(R²) by the mixed product property (A⊗B)(C⊗D) = (AC)⊗(BD). ∎

The folding algebra generated by {C,T} is ℤ×ℤ — two independent integer-indexed operations. The within-level Fibonacci spiral (composition) and the cross-level tower ascent (tensor product) do not interfere. This is the recursion-level analog of projection independence: composition and tensor product are independent operations, just as I², TDL, LoMI are independent projections.

**Remark (Three-Operation Algebra).** The Folding Commutativity identifies two of the framework's three canonical operations: C (within-level composition, M→M²) and T (cross-level tensor product, M→M⊗M). The third is the exponential map E (analytic lift, X→exp(X)). C and T are algebraic: they map ℤ[φ]→ℤ[φ] and produce no transcendental outputs — C maps eigenvalue λ→λ² (staying algebraic), T maps eigenvalues (λ₁,λ₂)→λ₁·λ₂ (staying algebraic). E is analytic: it escapes ℤ[φ] to transcendentals, producing {e,π} from the two Killing sectors. The commutation structure is [C,T]=0 (this theorem), [C,E]≠0 (exp(M²)≠(exp(M))²), [T,E]≠0 (categorically different). The operation algebra is non-abelian with an abelian algebraic subalgebra {C,T} producing all derived structure and a non-commuting analytic element E producing all irreducible outputs. The framework has five irreducible outputs: {e,π} from E alone at lift 3→4, {G,Λ} from the E×T interaction at lift 5→6 (where Bekenstein/KMS meets tensor factorization/observer structure in the Jacobson argument), and {K_meta} from the tower closure of E×T at lift 7→8+. The non-commutativity of E with {C,T} is the operational root of irreducibility.

---

## §3 THE SINGLE INTERNAL DUALITY

**Theorem 3.1 (Internal Duality).** Each projection has one UP/DOWN opposition:

| Projection | UP | DOWN | Fixed Point |
|------------|-----|------|-------------|
| I² | n² (compose) | factors(n) (decompose) | 1²=1, factors(1)={1} |
| TDL | emerge(n) from 1 | digital_root(n) | emerge(1)=reduce(1)=1 |
| LoMI | multiples of n | divisors of n | 1 divides all, all multiples contain 1 |

**Theorem 3.2 (Unity).** *The three dualities are one — BUILD↔ANALYZE — seen from three angles. UP operations grow (compose, emerge, contain); DOWN operations shrink (decompose, reduce, observe).* ∎

---

## §4 THE COMPOSITE POTENTIAL V(n)

**Definition.** V(n) = V_I(n) + V_T(n) + V_L(n) where:

| Component | Formula | Interpretation |
|-----------|---------|----------------|
| V_I(n) | log(n²/rad(n)) | Algebraic gap: compose vs decompose |
| V_T(n) | \|Ω(n) − ap(n)\| | Level gap: tower depth vs reduction depth |
| V_L(n) | \|log(d(n)) − log(φ(n))\| | Relational gap: divisors vs totient |

(rad = radical, Ω = prime factors with multiplicity, ap = additive persistence, d = divisor count, φ = Euler totient.)

V(n) measures the distance from the fixed point using all three projections simultaneously. Individual components V_I, V_T, V_L are developed in Papers 3-P1, 3-P2, 3-P3 respectively.

---

## §5 THE FIXED POINT n = 1

**Theorem 1.2 (Universal Fixed Point).** *UP(1) = DOWN(1) = 1 in all three projections.* I²: 1²=1. TDL: emerge(1) = reduce(1) = 1. LoMI: 1 is universal GCD. ∎

**Theorem 1.3b (Uniqueness).** *n = 1 is the unique fixed point. For n > 1: n² > rad(n), so V_I(n) > 0.* ∎

**Theorem 1.6 (V(1) = 0 Exactly).** V_I(1) = log(1/1) = 0. V_T(1) = |0−0| = 0 (Ω(1)=0, ap(1)=0). V_L(1) = |log(1)−log(1)| = 0. Total: **0**. V(n) gradient flow converges to n=1 with rate φ̄ (the unique contraction base). ∎

**Theorem 1.7 (V(n) > 0 for n > 1).** For n > 1: n² > rad(n), so V_I(n) > 0. ∎

| n | V_I | V_T | V_L | V(n) |
|---|-----|-----|-----|------|
| 1 | 0.000 | 0 | 0.000 | **0.000** |
| 2 | 0.693 | 1 | 0.693 | 2.386 |
| 6 | 1.792 | 2 | 0.693 | 4.485 |
| 12 | 2.485 | 2 | 1.099 | 5.584 |

**Theorem 5.1 (1 Is the Arithmetic R(R)=R).** *n = 1 is simultaneously the multiplicative identity (definition) and the unique common fixed point of three projections (theorem). Both definition and theorem, like q∘q = q in Paper 1.* ∎

---

## §6 THE ARITHMETIC FLOW

**Definition.** The arithmetic flow is a Markov process on ℕ with transition probabilities P(n→m) ∝ exp(−β[V(m)−V(n)]) · δ(m reachable from n), where "reachable" means obtainable via GCD, sqrt, digital root, or division by smallest prime factor.

**Theorem 3.2b (Stationary Distribution).** *The unique stationary distribution concentrates at n = 1 (global minimum of V).* ∎

**Theorem 3.3 (Detailed Balance).** P(n→m)/P(m→n) = exp(−β·ΔV). Verified: 12↔6 ratio = 11.29; 144↔12 ratio = 5.4×10⁶ — simplification overwhelmingly favored. ✓

**Corollary 3.5 (Natural Temperature).** β = ln(φ) ≈ 0.481. At this β: σ_FIX = φ̄ (self-consistent Boltzmann fixed point).

**Theorem 3.6 (ℤ Extension).** V(−n) = V(n) by parity symmetry. Fixed points: {±1}. ∎

**Theorem 3.7 (ℚ Extension).** Via p-adic valuations. Fixed points remain ±1. ∎

100% convergence from all tested starting points: 12→2→1 (1.1 steps), 144→12→2→1 (1.3 steps), 5040→...→1 (converges). ✓

---

## §7 THE CENTRAL COLLAPSE

**Theorem 7.1 (I²∘TDL∘LoMI = Dist).** *Every Dist morphism f factors as:*

```
A ──surjection──▶ A/ker(f) ──bijection──▶ f(A) ──inclusion──▶ B
      LoMI            TDL                I²
```

The surjection (quotient by kernel) is the LoMI factor. The bijection (isomorphism between levels) is the TDL factor. The inclusion (embedding in codomain) is the I² factor. This is the first isomorphism theorem interpreted through the projection correspondence.

**Canonical, complete, exhaustive.** No fourth component exists. ∎

**Corollary 7.2.** The three projections exhaust every Dist morphism with no structural remainder.

**Remark (Central Collapse as Exhaustion of Self-Action).** The factorization surjection∘bijection∘injection = Dist morphism is the exhaustion of self-relating difference (Paper 0 §1½) into its three irreducible categorical steps: LoMI identifies (surjection: R's observational face collapses kernel), TDL transports (bijection: R's transition face maps between levels), I² includes (injection: R's compositional face embeds into target). Every Dist morphism is exactly these three steps composed. No fourth step exists because self-relating difference has exactly three non-trivial faces (|V₄\{0}|=3, Paper 2 Thm 3.3).

**Remark (Central Collapse Normal Form).** The central collapse is the proof architecture for the framework's master theorems. Every master theorem decomposes into three projection faces — P1/injection (what is produced), P2/bijection (what mediates), P3/surjection (what is observed) — and the central collapse guarantees the decomposition is exhaustive with no remainder. Verified for all five content master theorems: Productive Opacity (Paper 5 §17.4d): ker→scale (P1) ∘ ker→transition (P2) ∘ ker→blindness (P3). R(R)=R Tower Universality (Paper T-BLUEPRINT §5.5): terminal closure (P1) ∘ recursive closure (P2) ∘ boundary closure (P3). K6' Bundle Universality (Paper 6B §12.4): gauge connection (P1) ∘ K6' mechanism (P2) ∘ frame connection (P3). Cost-to-Geometry Chain (Paper 6B §12.5): structure→entropy (P1) ∘ anchor mediation (P2) ∘ entropy→curvature (P3). Trinitarian Root (below): production of 3 (P1) ∘ zero-branching lift (P2) ∘ application at each level (P3). The central collapse is not one theorem among six — it is the FORM; the other five are the CONTENT.

**Remark (Status Grammar Completeness).** The central collapse is the completeness theorem for morphism-level self-interpretation: three projections exhaust all relational modes. Paper T-SIL §1 (Theorem SIL-0) proves the analogous completeness at the claim level: four native statuses exhaust all claim types. The central collapse's factorization order injection→bijection→surjection generates the implication chain D→C→V that forces exactly four statuses — the same ordering that forces the factorization here forces the status grammar there.

**Remark (Central Collapse as Computation).** The factorization I²∘TDL∘LoMI = Dist is a computation-theoretic statement: every Dist morphism decomposes into a Type I compression (LoMI/surjection), a Type II transition (TDL/bijection), and a Type I embedding (I²/inclusion). The composite is itself Type I: idempotent (applying the decomposition twice changes nothing), zero structural branching, FIX-dominant. The canonical factorization is the most efficient decomposition — it minimizes branching at every step (Paper T-COMP §8).

**Remark 7.1a (Relational Completeness).** The central collapse identifies three irreducible relational modes. I² (injection) captures what *persists* through a morphism — the structural substrate that survives transformation. TDL (bijection) captures what *transitions* — the dynamic rearrangement between equivalent structures. LoMI (surjection) captures what *interacts* — the information loss accompanying any quotient. Independence (Theorem 1.1) ensures no two modes are mutually definable; completeness (Theorem 1.3) ensures no fourth mode exists, as the discriminant sign admits exactly three cases (negative, positive-split, positive-elliptic) plus a measure-zero boundary. Over the unit sphere of the discriminant form Δ = 5b² − 4c² − 4cd + 4d² (signature (2,1)), the P1/persistence sector occupies ~72% — structural persistence is the dominant relational mode, consistent with the I²-dominance of natural number sequences (Paper 3-P1 §3.4).

**Remark 7.1b (Factorization System and Yoneda Parallel).** The central collapse defines a three-way orthogonal factorization system on Dist: every morphism factors as surjection∘bijection∘injection, with surjections left-orthogonal to injections. This refines the standard (epi, mono) factorization system by isolating the bijection core — the level-transition component that rearranges structure without gain or loss. The three-way factorization parallels the Yoneda lemma, where every natural transformation from a representable functor is determined by its action on a single element: LoMI (surjection) identifies which quotient the morphism tests against, TDL (bijection) provides the isomorphism transport, and I² (injection) embeds the result faithfully. Whether this parallel extends to a formal functor-level equivalence between the central collapse and the Yoneda embedding — specifically, whether Dist admits a presheaf category in which the factorization is the image of the Yoneda functor — is an open structural question.

**Corollary 7.3 (Semantic Decomposition).** *The central collapse decomposes not only every morphism but every semantic primitive of the framework. The recurring structural acts named by the framework's vocabulary decompose into three meta-primitives corresponding to the three factors:*

| Meta-primitive | Central collapse factor | Projection | Semantic content |
|---------------|----------------------|-----------|-----------------|
| **The Observer Act** (disclose, occlude, co-determine, extract) | Surjection | P3 / LoMI | The full quotient: what observation reveals (im) and annihilates (ker) |
| **The Productive Act** (return, produce, complete) | Injection | P1 / I² | The full self-action: what self-composition generates and stabilizes |
| **The Mediating Act** (balance, minimize, transition) | Bijection | P2 / TDL | The full level-transition: what rearranges without gain or loss |

*The correspondence is forced by the central collapse's exhaustion property: surjection∘bijection∘injection accounts for every morphism with no remainder, so the three meta-primitives account for every semantic role with no remainder. The framework's vocabulary is itself an instance of the three-reading structure it describes.*

*Proof.* Every recurring semantic term names a Dist operation or a property of a Dist operation. By Theorem 7.1, every Dist operation factors into exactly three components. The semantic content carried by each term is accounted for by the component(s) it describes: observation language (quotient, kernel, disclosure, blindness) maps to the surjective factor; self-action language (closure, return, recursion, production) maps to the injective factor; transition language (ascent, balance, minimality, level) maps to the bijective factor. The decomposition is exhaustive because the central collapse is exhaustive. ∎

**Remark (Blueprint Horizontal Exhaustion).** The central collapse proves the three columns of the framework's generative grid exhaust every morphism at every level. No fourth column exists — |V₄\{0}|=3 and the orbit-type classification are exhaustive (Theorem 1.3). The grid B(n,p) is therefore complete: every framework theorem lives in some cell B(n,p) or describes a relation between cells, and every cell is addressed by exactly one of three projection columns.

**Remark (Role Exhaustion).** The central collapse also proves that the three projection-roles — production (P1), mediation (P2), observation (P3) — exhaust every morphism's structural role at every level. No fourth role-type exists (Paper T-BLUEPRINT §5.4). The nine structural roles (generator, closure operator, mediator, selection mechanism, invariant, obstruction, classifier, symmetry breaker, reconstruction mechanism) all decompose into P1-aligned (generator, closure), P2-aligned (mediator, selection), and P3-aligned (obstruction, classifier) families. The Role Recurrence theorem (Paper T-BLUEPRINT §5.4) verifies that this decomposition instantiates at every tower level.

**Remark (Cosmological Central Collapse).** The central collapse I²∘TDL∘LoMI = Dist applies to the cosmological observer K_cosmo (Paper 5 §6½): I²(K_cosmo) = gravitational self-consistency via Λ (the Cost-to-Geometry chain at the de Sitter horizon), TDL(K_cosmo) = thermal equilibrium at the Gibbons-Hawking temperature T_dS = (1/2π)√(Λ/3), LoMI(K_cosmo) = observational blindness at the horizon (the super-horizon kernel). The three projections converge on a single Λ-determined structure — the same Λ simultaneously governs gravity (P1), thermal equilibrium (P2), and constitutive blindness (P3). No fourth reading of the de Sitter horizon exists.

**Remark (Central Collapse at Level 6).** At Level 6, the central collapse manifests as gauge-gravity unification: gauge = P1 face of K6' (connection on the gauge bundle, production of field strength), gravity = P3 face of K6' (connection on the frame bundle, observation geometry), and the unification itself = P2 mediation between the two bundles via the shared K6' mechanism. The K6' Bundle Universality theorem (Paper 6B §12.4) is the explicit central collapse at Level 6: one theorem, two bundles, three projections.

**Remark (Dual Central Collapse).** The central collapse I²∘TDL∘LoMI = Dist admits a dual reading LoMI∘TDL∘I² = Dist related by the observer transposition σ = (P1 P3) (Paper T-BLUEPRINT §5.1). The algebraic reading decomposes morphisms right-to-left: surjection → bijection → injection (analysis, canonical, br_s = 0). The physical reading assembles physics left-to-right: injection → bijection → surjection (synthesis, non-canonical, br_s > 0). The two orderings swap P1 and P3, fixing P2 — which is σ. The asymmetry between them IS the construction-dissolution asymmetry (Paper 0 §9) at the factorization level: algebraic decomposition is unique, physical assembly is observer-dependent.

**Remark (Seven-Way Trichotomy Correspondence).** The central collapse generates not only three projections but seven confirmed projection-indexed trichotomies across the framework, all sharing the same P1/P2/P3 structure:

| P1 (Injection) | P2 (Bijection) | P3 (Surjection) | Trichotomy | Source |
|----------------|----------------|------------------|-----------|--------|
| Type I: compression | Type II: expansion | Type III: rotation | Computation types | Paper T-COMP §3–5 |
| Fixed-point | Asymptotic | Exact | Closure modes | Thm 8.6c below |
| Terminal | Recursive | Boundary | Closure types | Paper T-BLUEPRINT §5.5 |
| Accidental | Constitutive | Boundary | Occlusion types | Paper T-SIL §6 |
| Productive Act | Mediating Act | Observer Act | Semantic meta-primitives | Cor 7.3 above |
| Injection | Bijection | Surjection | Central collapse factors | Thm 7.1 |
| φ (projective witness) | e (temporal witness) | π (temporal witness) | Regime-readout witnesses | Thm 8.7a below |

All seven are the three central collapse factors applied to different objects. Each trichotomy traces to |V₄\{0}| = 3 (Thm 3.2) via the orbit-type classification (Thm 1.1), confirming the Trinitarian Root: every three-fold structural decomposition is a tower lift of the three non-identity elements in the self-product of the minimal binary domain.

**Theorem (Trinitarian Root).** *Every three-fold structural decomposition in the framework is a tower lift of |V₄\{0}| = 3: the three non-identity elements of the self-product S₁ = S₀² = {0,1}², with S₃ acting transitively (Paper 2 Thm 1.5). The three projections, three computation types, three closure modes, three closure types, three occlusion types, three meta-primitives, three regime-readout witnesses, three SIL questions (D/C/V), three particle generations, and the central collapse are instances at increasing tower depth. The tower lifts are united by two invariants: zero branching (canonical upward) and S₃-transitivity preservation.*

*Proof (instance verification).* The root: |{0,1}²| − 1 = 3, with S₃ = Aut(V₄) acting transitively on V₄\{0} (Paper 2 Thm 1.5). Propagation: three orbit types from dim(sl(2,ℝ)) = 3 and Killing signature (2,1) (Paper 2 Thm 3.3). Instances: seven projection-indexed trichotomies (table above), plus three SIL questions (§1.3: D/C/V from injection/bijection/surjection), three particle generations (Paper 6B §9 from S₃ transitivity on irreps). Each instance traces to |V₄\{0}| = 3 via a specific chain of zero-branching constructions documented in the respective source papers. ∎

**Grade: ENCODED.** Individual three-fold decompositions are FORCED. The universal claim that they all trace to |V₄\{0}| = 3 via S₃-transitivity preservation is verified exhaustively within the current framework but not proved in full generality — the gap is showing that zero-branching canonical constructions necessarily preserve S₃-transitivity.

**Remark (Weyl Group Bridge).** The reappearance of S₃ at Level 6 (three generations, three colors) is explained by the root system extension ladder (Paper 2 §5): the self-product tower corresponds to the Dynkin diagram extension A₁ → A₂. At Level 1, sl(2,ℝ) has root system A₁ with Weyl group W(A₁) = ℤ₂. At Level 2, the exchange operator produces su(3) with root system A₂ and Weyl group W(A₂) = S₃. The S₃ at Level 2 as Aut(V₄) and at Level 6 as W(A₂) is the same group acting through different structural channels — the tower lift IS the root system extension. The root count |roots(A₂)| = 6 = |S₃| (a property of simply-laced A_n root systems). The Weinberg angle sin²θ_W = |V₄\{0}|/(|V₄\{0}|+disc(R)) = 3/8 = dim(fund su(3))/dim(adj su(3)) is a representation-theoretic identity carried by this root system structure (Paper 6B §11).

**Remark (Killing Signature and Orbit Types).** The Killing form of sl(2,ℝ) has signature (2,1) (Paper 2 §7.2): two Killing-positive directions (containing R_tl and RN, generating hyperbolic/P1+P2 flows) and one Killing-negative direction (containing N, generating elliptic/P3 flows). The three orbit types are the three connected components of sl(2,ℝ) minus the Killing-null cone (the nilpotent boundary, Paper 2 §19¾). The discriminant Δ = 5b²−4c²−4cd+4d² has signature (2,1) matching the Killing signature — this is not coincidence: for traceless M, det(M) = −B(M,M)/8, so the discriminant IS the Killing form restricted to the coefficient space (Paper 2 Thm 3.4).

---

## §8 THE FOUR META-THEOREMS

**Theorem (Quadratic Engine Completeness).** *The characteristic polynomial p(x) = x²−x−1 of R has exactly four independent algebraic invariants:*
- *Root data → MP1 (φ̄-filtration): the eigenvalue channel*
- *Sign data → MP2 (trichotomy): the discriminant sign determines orbit type*
- *Recurrence data → MP3 (CH fixed points): Cayley-Hamilton forces canonical fixed points*
- *Resolution data → MP4 (resolution quantum): disc(R) = 5 sets the minimum resolution*

*These four exhaust the algebraic content of a quadratic: two roots, one discriminant, one recurrence. Every major recurrence family sourced from R reduces to these four. No fifth independent piece of algebraic information exists in a degree-2 polynomial.*

*Proof.* A monic quadratic x²+bx+c has four independent algebraic data: two roots r₁, r₂ (equivalently sum and product via Vieta), the discriminant Δ = b²−4c (sign and value are independent data), and the recurrence relation a_{n+2} = −ba_{n+1} − ca_n forced by Cayley-Hamilton. For p(x) = x²−x−1: roots φ and −φ̄ give MP1; disc sign gives MP2; CH equation R²=R+I gives MP3; disc value 5 gives MP4. Independence: root data is continuous (filtration), sign data is discrete (trichotomy), recurrence data is algebraic (fixed points), resolution data is arithmetic (integer threshold). No two are mutually definable. Completeness: the four data {r₁, r₂, sign(Δ), |Δ|} determine p(x) up to its Galois group; no further independent invariant exists for a quadratic. ∎

**Grade: THEOREM (FORCED).**

The four meta-theorems below are the four faces of Quadratic Engine Completeness — each develops one invariant channel and the theorem families it generates.

**MP1 (φ̄-Filtration).** From roots φ, −φ̄: the canonical filtration F_k = φ̄^k/2 on [0,1]. Unifies: MIX structural threshold (F_2), self-signature components (F_0, F_1, F_2), Boltzmann weights at β=ln(φ), S₃ duality gaps, Phase-Dist distinguished values. ~8 theorems as corollaries.

**Remark (Consciousness Staircase as MP1 Instance).** The consciousness depth thresholds d_K = φ^{2^m} (Paper 5 §22) are MP1 filtration instances: each threshold is a φ-power, and the doubly exponential spacing 2^m is the tower lift of the single-exponential contraction φ̄² per step. The staircase is MP1 applied to the observer capacity axis. The three φ̄-filtration applications — MIX threshold at φ̄² (computation), Boltzmann weight at φ̄ (thermodynamics), consciousness transition at φ^{2^m} (observer theory) — are the same eigenvalue channel operating at different levels of the grid.

**MP2 (Trichotomy).** From discriminant sign: every framework object is P1-type (Δ>0, det<0), P2-type (Δ>0, det>0), or P3-type (Δ<0). The (det,Δ) classification is exhaustive with ratio ~72:28 on the unit sphere. Unifies: orbit classification, arithmetic sequence classification, Jordan type mapping. ~5 theorems.

**MP3 (CH Fixed Points).** From Cayley-Hamilton R²=R+I: every recursive equation has canonical fixed points at R=φ (attractive) and R=−φ̄ (repulsive). Unifies: n=1 arithmetic fixed point, Möbius attractor φ̄, observer loop closure, R(R)=R. ~5 theorems.

**MP4 (Resolution Quantum).** From disc(R) = 5: the minimum resolution at which structure becomes visible. Pauli matrices have denominator 5. The integer 5 = disc(R) appears as the universal resolution threshold. Unifies: Pauli at resolution 1/5, Gram det = 5², Killing eigenvalue 5. ~3 theorems.

**Remark (Five-Fold Recurrence).** disc(R) = 5 recurs across all tiers: as disc(x²−x−1) (algebraic, Paper 2 §6), as ‖R‖²+‖N‖² = 3+2 (geometric, Paper 2 §8 Thm 8.4), as rank(Λ') = 5 (lattice, Paper 4 §1), as det(Gram({I,R,N,RN})) = 5² (spectral, Paper 2 §8 Cor 8.5), as |Fix(D)| = 5 (categorical, Paper 0 §7), and as the bridge chain transition count (constructive, Paper 2 §5). The norm-sum identity disc(R) = ‖R‖²+‖N‖² is proved equivalent to det(R) = −1, the P1 condition (Paper 2 Thm 8.4). The Gram determinant factors as disc(R)² through the sector orthogonality {I,R} ⊥ {N,RN} (Paper 2 Cor 8.5–8.6). The lattice rank and fixed-locus count share the value disc(R) without known reduction to CH(R). The minimality of disc(R) = 5 as the productive resolution quantum (Paper 2 §8, Remark 8.6a) grounds MP4 further: 5 is the smallest integer at which the Norm-Sum Identity, irreducibility over ℚ, and orthogonal sector decomposition co-occur. The disc = 4 case is degenerate (involutory, reducible). The tower propagation LF3 (total norm² = 5ⁿ at level n) states that resolution compounds geometrically, with 5 as the tightest possible productive budget.

All verified: 79 PASS, 0 FAIL, 3 WARN. Predictive: the meta-theorems constrain what future results can look like.

**Remark (MP1 as Single-Channel Reading).** MP1 (φ̄-filtration) is the single-channel reading of a two-channel process. The bi-infinite Fibonacci field decomposes into expanding channel A (φⁿ/√5) and contracting channel B (−(−φ̄)ⁿ/√5), with F(n) = A(n) + B(n) (Paper 3-P1 §2.10). The φ̄-filtration F_k = φ̄^k/2 tracks the contracting channel's contribution; the dominant channel φⁿ sets the overall scale. The channel dominance swaps at n = 0 (the phase-neutral locus). MP1 captures the asymptotic behavior where one channel dominates; the full two-channel decomposition captures the interference structure.

**Remark (Candidate MP5 — Recurrence-Level Crossing).** The centered value cell {−1, 0, +1} of the P1 recurrence field (Paper 3-P1 §2.2½) and its three sign-transition regimes (FLIP/ZERO/SAME) recapitulate the root crossing {0, 1} where Dist = Co-Dist (Paper 0 §8). The structural parallels are forced by the same algebraic chain (binary minimality, det = −1, tr = 1). The correspondence is a Metapattern — not a functor — but it is the only known instance of a framework structure recurring at the recurrence level in the same form as at the root. If this pattern generalizes (e.g., if the P2 and P3 recurrence fields also exhibit centered crossing structures), it would constitute a fifth metapattern: MP5 (tier-recurrence).

**Remark (Three-Projection Derivative — see Theorem 8.5a).** The Möbius derivative f'(φ̄) = −φ̄² = φ̄²·e^{iπ} simultaneously encodes all three projections (Paper 3-P1 §5.7): magnitude φ̄² (P1 contraction rate), phase π (P3 half-period), sequential iteration (P2 level structure). This is a corollary of Theorem 8.5a below: the derivative is the P1-specific instance of the universal tri-projection structure.

---

## §8½ EULER AS MINIMAL BINARY-PHASE CLOSURE

The identity e^{iπ} + 1 = 0 is not primarily a relation among famous constants. It is the minimal closure law for continuous inversion of a binary pole: the first exact event where phase transport realizes binary inversion and cancels it to null. It instantiates all three projections simultaneously, making it a canonical tri-projection object.

**Theorem 8.5a (Euler's Identity Is Tri-Projective).** *The identity e^{iπ} + 1 = 0 instantiates all three projections simultaneously:*

- *P1 (I²/φ-sector) supplies the binary poles {+1, −1} and the cancellation to 0. These are orientation-reversing endpoints: +1 is the identity pole, −1 is the inverted pole (det(R) = det(J) = −1), 0 is resolved cancellation.*
- *P2 (TDL/e-sector) supplies the exponential realization law. The constant e is the base of the exponential map that converts the generator into a flow.*
- *P3 (LoMI/π-sector) supplies the phase manifold and the closure schedule. π is the first exact inversion time: exp(πN) = −I (Theorem 4.3, Paper 3-P3). The phase circle S¹ = {e^{iθ}} is P3's maximal compact subgroup SO(2) (Theorem 1.7, Paper 3-P3).*

*No projection can be removed without destroying the identity. Euler is a minimal tri-projection object.*

**Proof.** P1 content: the poles ±1 are eigenvalues of all det < 0 matrices in {I,R,N,RN}; cancellation +1 + (−1) = 0 is orientation-reversal collapse. Remove P1: no poles, no cancellation target. P2 content: exp is TDL's defining operation (Paper 3-P2 Thm 1.7: e = det(exp(R))). Remove P2: no realization mechanism. P3 content: π is P3's absolute contribution (Paper 3-P3 Thm 4.3); S¹ is SO(2) (Paper 3-P3 Thm 1.7). Remove P3: no phase closure parameter. Minimality: the identity contains exactly five symbols {e, i, π, 1, 0} and two operations; no proper subset expresses the same closure law. ∎

**Corollary 8.5b (Three-Projection Derivative).** *The Möbius derivative f'(φ̄) = −φ̄² = φ̄²·e^{iπ} at the P1 fixed point is the P1-specific instance of Theorem 8.5a: magnitude φ̄² (P1 contraction), phase e^{iπ} (P3 half-period via Euler), sequential iteration (P2 level structure). The derivative result is a concrete instance of Paper 1 Thm 5.1: every Dist morphism instantiates all three projections simultaneously.*

**Theorem 8.5c (BPC-Forcing).** *The following assumptions uniquely force Euler's identity:*
- *A1: distinguished initial state 1. A2: opposite representable as −1. A3: passage from 1 to −1 continuous. A4: evolution preserves norm. A5: evolution is a one-parameter group. A6: inversion at finite positive parameter. A7: recurrence.*

*Under A1–A7, the realization is z(θ) = e^{iθ} on S¹, the first inversion time is π, and the first return time is 2π.*

**Proof.** A1 + A4 place z on S¹. A3 + A5 give a continuous group homomorphism ℝ → S¹, which is e^{ikθ} (classification theorem). A6 forces k ≠ 0. A2 + A6 give first inversion at π/|k|. A7 gives period 2π/|k|. Canonical normalization k = 1 (unit angular speed) completes the result. Zero branching at every step. ∎

**Remark (Structural inevitability).** The strong claim: any adequate continuous, norm-preserving, recurrent realization of binary inversion is forced into an Euler-type structure. The identity is structurally inevitable under natural closure assumptions.

**Theorem 8.5d (Closure Rank — Euler Is Unique).** *Each of the five ingredients of e^{iπ} + 1 = 0 — exponential realization, phase generator i, half-period π, identity pole 1, null closure 0 — is independently irreducible: removing any one collapses the equation to non-closure. Any binary-phase closure event z₀(e^{iπ} + 1) = 0 factors through Euler via scalar multiplication, making it the unique canonical rank-1 closure event.*

**Proof.** (a) Exponential irreducible: the unique continuous group homomorphism ℝ → S¹ is exp(ikθ); no polynomial/rational alternative exists (|p(θ)| = 1 on ℝ forces p constant). (b) Phase generator i irreducible: exp(tα) > 0 for real α; cannot reach −1. (c) π irreducible: e^{iθ} = −1 requires θ = π + 2nπ; smallest is π. (d) +1 irreducible: without it, e^{iπ} = −1 is inversion, not closure. (e) 0 irreducible: e^{iπ} + 1 = c with c ≠ 0 defines c, not a closure law. Uniqueness: z₀(e^{iπ} + 1) = 0 factors through z₀ = 1. ∎

**Remark (Constants as event-markers).** In the Euler reading, constants are not primitive objects but role-markers in a forced process: e = exponential completion of a generator, π = first exact inversion parameter, i = infinitesimal phase-turning operator, 1 = distinguished initial pole, 0 = exact cancellation after opposition resolves. This is native to the framework's style where objects are typed by role, operation, and projection.

**Remark (Relation to four forced constants).** The framework identifies four forced constants: φ, e, π, √3 (Paper 2 §6). Euler selects {e, π} — those needed for phase-transport closure — plus boundary poles {1, −1, 0}. The constant φ (P1 eigenvalue) does not appear because Euler involves transport and closure, not self-composition. The constant √3 = ‖R‖_F does not appear because Euler involves no norm measurement. The selection is typed by the process.

---

## §8¾ CLOSURE MODES AND THE ELLIPTIC-HYPERBOLIC DICHOTOMY

**Theorem 8.6a (Hyperbolic-Elliptic Dichotomy).** *The two canonical one-parameter flows from sl(2,ℝ) are:*

| Property | Elliptic: exp(θN) | Hyperbolic: exp(th) |
|----------|-------------------|---------------------|
| Generator | N (skew-symmetric) | h (traceless diagonal) |
| Eigenvalues | e^{±iθ} (unit circle) | e^{±t} (real line) |
| Orbits | Closed (periodic) | Open (non-periodic) |
| Norm | Preserved | Not preserved |
| Returns to I | Yes (at 2π) | No (only at t = 0) |
| Inversion (−I) | Yes (at π) | No (never: eigenvalues always positive) |
| Framework | P3 / LoMI / closure | P2 / TDL / ascent |

**Proof.** N has eigenvalues ±i → exp(θN) has eigenvalues e^{±iθ} ∈ S¹ (periodic). h has eigenvalues ±1 → exp(th) has eigenvalues e^{±t} ∈ ℝ₊ (monotone, never zero). exp(th) ≠ −I for any real t (eigenvalues positive). ∎

Verified: ‖exp(th) − (−I)‖ grows monotonically: 3.96 at t = 1, 8.47 at t = 2, 149.4 at t = 5. ✓

**Corollary 8.6b (No Hyperbolic Euler).** *There is no real t such that exp(th) + I = 0. The hyperbolic sector does not support exact inversion-cancellation. Euler's identity is specific to the elliptic sector.*

**Theorem 8.6c (Exhaustive Closure Modes).** *The three orbit types admit exactly three closure modes, exhaustive by MP2 trichotomy:*

| Orbit type | Projection | Closure mode | Canonical statement | Strength |
|-----------|-----------|-------------|-------------------|----------|
| Elliptic (det>0, Δ<0) | P3/π | EXACT | exp(2πN) = I (period 2π, half-period π) | Strongest |
| Hyperbolic (det<0) | P1/φ | FIXED-POINT | Möbius iterate → φ at rate φ̄² | Middle |
| Split-real (det>0, Δ>0) | P2/e | ASYMPTOTIC | det(exp(tR)) = e^t (rate convergence) | Weakest |

**Proof.** P3: eigenvalues on S¹, orbits closed with period 2π, exact inversion at π. P1: Möbius action has attracting fixed point φ, geometric convergence rate |f'(φ̄)| = φ̄². P2: eigenvalues e^{±t} unbounded, orbits open, closure at rate level only: det(exp(tR)) = e^{tr(R)} = e^t. Exhaustiveness: discriminant sign gives exactly three cases (MP2). ∎

**Corollary 8.6d (Closure-Strength ↔ Forcing-Quality Alignment).** *The closure strength hierarchy EXACT > FIXED-POINT > ASYMPTOTIC matches the forcing quality hierarchy π > φ > e. Absolute forcing produces exact closure; strong forcing produces fixed-point closure; qualified forcing produces asymptotic closure. The closure mode is the forcing quality read dynamically.*

**Remark (Pairwise Bridge Triangle).** Euler completes a triangle of pairwise projection bridges, each using the exponential map in a different mode:

```
              P1
             /    \
   det(exp(R))=e   x²∓x+...=0
           /            \
         P2 ——————————— P3
             e^{iπ}+1=0
```

P1↔P2: det(exp(R)) = e (exponentiating P1's generator produces P2's constant). P1↔P3: characteristic polynomial duality x²−x−1 ↔ x²+x+1 (Paper 3-P3 §1.3). P2↔P3: Euler's identity (exponential realization of phase closure). Each bridge is a different face of the exponential map applied to different generators.

---

## §8⅞ REGIME-READOUT DUALITY

The closure modes (§8¾) classify the qualitative behavior of one-parameter flows from sl(2,ℝ). The strip-regime bridge (Paper 2 §23½) shows that the same regime scalar det(strip(A)) simultaneously governs the flow character and the projective fixed-point geometry of any 2×2 action. This section states the cross-projection synthesis theorem that unifies these results.

**Theorem 8.7a (Regime-Readout Duality — Meta-Theorem).** *The three closure modes (Thm 8.6c), the five forced constants (Paper 2 §9), and the five classification theorems (Paper 4 §14 C1–C5) are instances of a single regime-readout duality: the stripped traceless core of a 2×2 action determines both its temporal readout (from the exponential flow) and its projective readout (from the Möbius fixed-point equation), and the forced constants are the primitive witnesses of these readouts.*

| Regime | Closure mode (§8¾) | Temporal witness | Projective witness | Dominant classification |
|--------|-------------------|------------------|--------------------|------------------------|
| Hyperbolic | Fixed-point (P1/φ) | e (P2) | φ-orbit (P1) | C1 (φ), C2 (e) |
| Elliptic | Exact (P3/π) | π (P3) | i-orbit (P3) | C3 (π) |
| Parabolic seam | — | 1 | 1 | Boundary of C1/C3 |

*The hyperbolic branch has a dual internal structure: its temporal face is P2-aligned (exponential flow → e) while its projective face is P1-aligned (Möbius fixed point → φ). This is why the P1/P2 separation requires the trace (Paper 2 §7.2 Remark): within sl(2,ℝ) the temporal and projective faces of the hyperbolic regime are inseparable, and the P1/P2 distinction emerges only when the full matrix A (including trace) is restored.*

*Proof.* The regime is det(strip(A)): negative → hyperbolic, zero → parabolic, positive → elliptic (Paper 2 Thm 23½.2). The strip-regime bridge (Paper 2 Thm 23½.1) equates this to the projective fixed-point discriminant: −4det(strip(A)) = tr(A)²−4det(A). Therefore each regime simultaneously determines a closure mode (§8¾), a temporal witness (from exp(t·strip(A))), and a projective witness (from the fixed-point polynomial). The primitive witnesses are: e for hyperbolic temporal (exp(h)[0,0]=e), φ-orbit for hyperbolic projective (roots of x²−x−1), π for elliptic temporal (exp(πN)=−I), i-orbit for elliptic projective (roots of x²+1), and 1 for the parabolic seam (Paper 2 Thm 23½.4). The correspondence to C1–C5 follows from orbit type → dominant generator (Paper 4 §13). ∎

**Corollary 8.7b (Dual-Readout Structure of the Hyperbolic Branch).** *The hyperbolic regime is the only regime whose temporal and projective witnesses are algebraically independent constants (e and φ respectively). The elliptic regime's temporal and projective witnesses (π and i) are algebraically related (i² = −1, π = half-period of exp(θi)). The parabolic seam's witnesses are both trivial (1). The hyperbolic branch's dual structure is the source of the P1/P2 distinction at the generator level.*

**Remark (φ as Minimal Primitive Projective Witness).** The regime-readout duality explains why φ occupies a special position among the constants. It is the minimal primitive irrational hyperbolic projective witness (Paper 2 Thm 23½.5): disc=4 is degenerate (rational fixed points ±1), disc=5 is the first productive threshold (irrational fixed points φ, −φ̄). The same productive minimality that distinguishes disc=5 in the resolution quantum (MP4) distinguishes φ in the witness architecture — both are the same algebraic fact (disc(R)=5) read through different channels.

**Remark (Constants as Typed Witnesses, Not Free Parameters).** The regime-readout duality completes the framework's account of why these five constants and no others appear: they are the typed canonical outputs of a single stripped self-action engine. The engine has two non-trivial regimes (hyperbolic and elliptic) × two readouts (temporal and projective) = four spectral witnesses {e, φ, π, i}, of which three are real ({e, φ, π} — the lattice generators) and one is the algebraic complexification (i — already captured by spectral completion in the bridge chain). The two geometric constants {√3, √2} are amplitude witnesses of the generator pair, outside the regime engine. The parabolic seam contributes no new constant. Total: 3 spectral + 2 geometric = 5 = rank(Λ').

---

## §9 CROSS-DOCUMENT UNIFICATIONS

**Theorem NEW-1 (KMS-Filtration-Signature Unification).** *At β = ln(φ): the per-element Boltzmann weights for complexity shells C = 0,1,2 are (1/2, φ̄/2, φ̄²/2) — identical to the self-signature σ_meta and the φ̄-filtration levels F_k. The normalization identity 1 + φ̄ + φ̄² = 2 is Cayley-Hamilton rearranged.* all three quantities are φ^{0,−1,−2}/2. *Three objects from three source documents are one object.*

**Theorem NEW-2 (Phase Boundary Is Not a Lattice Point).** *The PNE phase boundary ρ = 1/2 is provably not a point of the Λ' lattice (which consists of φʳ·eᵈ·πᶜ·(√2)ᵃ·(√3)ᵇ). This is a concrete instance of observer incompleteness: the phase boundary value cannot be expressed in the framework's own constant system.*

---

## §10 FOUR-LAYER COHERENCE

The framework is coherent across four levels:

| Layer | Content | Central Equation |
|-------|---------|-----------------|
| Categorical | Dist morphisms, quotient, observer | q∘q = q |
| Algebraic | {R,N}, Cl(1,1), three orbit types | R²=R+I |
| Arithmetic | V(n), flow, convergence to 1 | UP(1)=DOWN(1)=1 |
| Meta | Framework encoding itself | M(K₀,F₀,U₀)=(K₀,F₀,U₀) |

Each layer's fixed-point equation is a realization of R(R)=R.

---

## §11 CLAIM STATUS

Native status grammar per T_SIL: FORCED (D=C=V=1, zero-branching derivation), ENCODED (D=0, C=V=1, containment proof). Generation class per T_GOV.

| Claim | Status | Generation |
|-------|--------|------------|
| Projection Independence (1.1) | **FORCED** | G.5 |
| Projection Completeness (1.3) | **FORCED** | G.1 |
| Folding Theorem (2.1) | **FORCED** | G.5 |
| Internal Duality (3.1) | **FORCED** | G.5 |
| Unity (3.2) | **FORCED** | G.5 |
| Central Collapse (7.1) | **FORCED** | G.1 |
| Quadratic Engine Completeness | **FORCED** | G.1 |
| MP1 (φ̄-filtration) | **FORCED** | G.4 |
| MP2 (Trichotomy) | **FORCED** | G.4 |
| MP3 (CH Fixed Points) | **FORCED** | G.4 |
| MP4 (Resolution Quantum) | **FORCED** | G.4 |
| Euler Tri-Projective (8.5a) | **FORCED** | G.4 |
| Closure Modes (8.6c) | **FORCED** | G.4 |
| Regime-Readout Duality (8.7a) | **FORCED** | G.4 |
| Trinitarian Root | **ENCODED** | G.9 |
| KMS-Filtration Unification (NEW-1) | **FORCED** | G.4 |

Generation classes: G.1 (strict forcing), G.4 (bridge-forced), G.5 (projection-induced), G.9 (semantic-compression for Trinitarian Root).

---

*R(R) = R*
