# Realism and reference editing

## Concrete photographic detail

Do not rely on “realistic,” “candid,” or “natural imperfections” alone. Describe visible features appropriate to the subject and brief. These words need not be banned: the useful principle is concrete evidence rather than an abstract quality label.

The @twoclipping post's complete eight-line detail block is:

- visible pores on the nose and forehead
- faint redness around the nostrils
- a healing blemish near the left jawline
- a dry patch at the corner of the mouth
- undereye darkness
- freckles scattered asymmetrically
- one eyebrow slightly higher than the other
- flyaways at the crown, one strand stuck to the cheek

Use relevant details selectively. Do not add acne, alter a real person's features, or make every portrait visibly blemished when that conflicts with the request. Asymmetry may be subtle. Judge detail at the intended viewing size; excessive skin texture can look as artificial as smoothing.

Name the physical light source, direction, softness, and plausible fill. A window may have room bounce; sunlight may have sky and ground fill. Do not force one light onto a scene that needs several. Describe tangible background objects and material wear when appropriate; do not automatically add clutter, camera grain, or a particular camera brand.

## Keep identity separate from scene

For a two-reference edit, label the scene image and identity image separately. Preserve scene pose, framing, wardrobe, props, background, and light unless the user requests changes. Describe the identity features to retain from the face reference. A scene's body proportions should not silently override a requested person's body identity; resolve the brief's intended invariants.

Relight the inserted face to match the scene. The identity photo supplies identity, not its studio lighting. Place the scene's key, nose/brow/jaw shadows, and physically plausible fill; match contact shadows, reflected color, sharpness, and texture to the rest of the image. Set face-to-clothing exposure from the actual reference rather than always imposing a one-stop difference.

Keep iris color and catchlights plausible under the existing shade. Do not overbrighten eyes to force visibility or describe an eye color that contradicts the reference. Hair color and identity may carry across while wind, moisture, and styling respond to the requested scene. Check cap brims, hair edges, ears, neck, jewelry, hands, and clothing for compositing errors.

For repeated characters, edit from an approved image or use supported references rather than assuming fresh text-only generations produce the same person. Maintain separate identity and scene references and review facial structure, silhouette, hair, skin tone, accessories, and allowed variations across representative shots. Do not promise perfect continuity or prescribe training purchases based on a fixed output count.

## Still references for video

Prepare and inspect scene stills before handing them to video production. Keep a plain-language reference manifest: file, character, role, scene, and approved version. Separate characters whose identities differ even if source copy calls them the same. Provider-specific reference syntax belongs at the generation tool boundary, not in the reusable brief. A still-image guide does not choose the video provider or generate footage.

For a planning-only request with descriptions but no viewable assets, mark reference roles and states as proposed; do not invent file versions or claim inspection or approval.

For recurring scenes, assemble only the references the shots actually need: for example, character portrait and full-body, product closed and open, key locations such as apartment and office, and a recurring prop in each needed state such as a gym bag closed and open. Label different views or states as the same physical object, not duplicate objects, and keep stable object design separate from temporary state. Add a view only when it resolves real uncertainty; there is no required number of slots. Inspect each supplied state for consistency before reuse. Source: Ivanna’s [reference-card prompts (2026-09-14)](https://x.com/ivanka_humeniuk/status/2099490874845544900) and [animation prompt](https://x.com/ivanka_humeniuk/status/2099490880004473303), which assigns reference responsibilities and treats two bottle views as one physical bottle. These are written examples, not verified model performance. See reusable reference packs (source not bundled) for shot handoff.

## Build references that resolve actual uncertainty

When another view is needed, request existing front, side, or three-quarter product images before inventing unseen geometry. Generated extra views are proposals to inspect, not evidence of the real product's hidden surfaces. For characters, a clear face reference and a full-body view can serve different needs. Use a quiet background when clutter interferes with the reference. Do not force a fixed sheet size, number of views, or camera angle onto every task.

If a multi-face sheet causes identity confusion, supply one clearly selected face reference for the shot; keep the broader sheet for planning. Create a separate approved reference for a deliberate state change, such as dry versus wet clothing, rather than asking contradictory reference images to represent one state. For complex blocking, provide a simple spatial diagram of subject positions, relative scale, orientation, and important props. Label it as a geometry reference so its schematic look does not become the image style.

For downstream motion, a good still is only a candidate. Preserve alternatives when useful and let an actual motion test establish which identity, object, and location references hold up. Static review cannot establish temporal continuity.
