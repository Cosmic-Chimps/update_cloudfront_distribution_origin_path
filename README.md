# Update Cloudfront distribution s3 origin path action

This action prints "Hello World" or "Hello" + the name of a person to greet to the log.

## Inputs

### `distribution-id`

**Required** CloudFront Distribution Id.

### `s3-origin-path:`

**Required** New S3 Origin Path.

### `origin-index`

**Required** Origin Index.


## Example usage

```
uses: actions/upload_cloudfront_distribution@v1
with:
    distribution-id: ${{ env.CLOUD_FRONT_DISTRIBUTION_ID }}
    s3-origin-path: ${{ env.GITHUB_RUN_ID }}
    origin-index: 0
env:
    AWS_REGION: ${{ secrets.S3_AWS_DEFAULT_REGION }}
    AWS_ACCESS_KEY_ID: ${{ secrets.CLOUD_FRONT_S3_AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.CLOUD_FRONT_S3_AWS_SECRET_ACCESS_KEY }}
```
