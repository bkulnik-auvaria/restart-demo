
provider "aws" {
  profile = "...." # <---- setup your user here
  region  = "eu-central-1"
}




resource "aws_s3_bucket" "restart" { # Deploy this first
  bucket = "restart-bucket-1234839934"
}

resource "aws_s3_bucket" "restart2" {
  bucket = "restart-bucket-1234839935"
}

resource "aws_s3_bucket_public_access_block" "restart" {
  bucket                  = aws_s3_bucket.restart.bucket #  deploy this second
  ignore_public_acls      = true
  restrict_public_buckets = true
  block_public_acls       = true
  block_public_policy     = true
}

resource "aws_s3_object" "name" {
  bucket  = aws_s3_bucket.restart.bucket
  key     = "hello.txt"
  content = "hello world!"
}







resource "aws_iam_user" "restart_user" {
  name = "restart-test-user"
}

resource "aws_iam_access_key" "restart_user" {
  user = aws_iam_user.restart_user.name
}


resource "aws_iam_policy" "restart" {
  name   = "RestartBucketAccessPolicy"
  policy = data.aws_iam_policy_document.bucket_access.json
}

data "aws_iam_policy_document" "bucket_access" {
  statement {
    effect = "Allow"
    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:ListBucket"
    ]
    resources = [
      aws_s3_bucket.restart.arn,       # <-- arn:aws:s3:::restart-bucket-1234839934
      "${aws_s3_bucket.restart.arn}/*" # <-- arn:aws:s3:::restart-bucket-1234839934/*
    ]
  }
}

resource "aws_iam_user_policy_attachment" "restart" {
  user       = aws_iam_user.restart_user.name
  policy_arn = aws_iam_policy.restart.arn
}


######################################################
# %%    Outputs
######################################################

output "bucket_name" {
  value = aws_s3_bucket.restart.bucket
}

output "access_key_id" {
  value = aws_iam_access_key.restart_user.id
}

output "secret_access_key" {
  value = nonsensitive(aws_iam_access_key.restart_user.secret)
}
