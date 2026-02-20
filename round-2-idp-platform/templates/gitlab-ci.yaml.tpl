stages:
  - build
  - deploy

build:
  script:
    - docker build -t $CI_REGISTRY_IMAGE .
